#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#  erika.py
#  
#  Copyright 2022  <sven@muehlberg.net>
#  
#  

import struct
from typing import Optional

# import sys
import serial
import time

import threading,os,stat

import evdev
from evdev import ecodes as e

from erika.erika2uinput import erika2uinput as e2i


def signed_byte(value):
    return struct.pack("b", value)


class Erika:
    def __init__(self, serdev, baudrate, rtscts, setperm, verbose):
        self.serial          = serial.Serial()
        self.serial.port     = serdev
        self.serial.baudrate = baudrate
        self.serial.rtscts   = rtscts
        self.lpsetperm       = setperm
        # stats
        self.alive           = None
        self.threads         = []
        self.verbose         = verbose
        self.kbd_name        = 'Erika devel 0.1'
        self.echo            = False
        # debug

    def open(self):
        self.serial.open()

    def close(self):
        self.serial.flush()
        # time.sleep(5)
        self.serial.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    ##########################

    def read(self) -> bytes:
        """read bytes[0] (one byte) from serial"""
        return self.serial.read()

    def write(self, data: bytes) -> Optional[int]:
        """write byte array to serial"""
        return self.serial.write(data)
    
    ##########################
    
    def start_lp(self):
        """Start lp thread"""
        thread=threading.Thread(target=self.lp,name='lp')
        thread.daemon = True
        thread.start()
        self.threads.append(thread)        
        
    def start_kbd(self):
        """Start kbd thread"""
        # start serial->console thread
        thread=threading.Thread(target=self.kbd, name='kbd')
        # thread gets killed when programs exit 
        thread.daemon = True
        thread.start()
        self.threads.append(thread)
        
    def lp(self):
        """loop and copy pts->serial"""
        # create pts and print name (later link it"""
        master,vserial = os.openpty()
        vs_name = os.ttyname(vserial)
        if not not self.lpsetperm: # not empty string
            os.system(self.lpsetperm + " " + vs_name)
            if self.verbose:
                print("starte",self.lpsetperm)
        if self.verbose:
            print("erika-device :",vs_name)
        try:
            os.set_blocking(master,False)
            while self.alive:
                try:
                    data = os.read(master,1)
                    if len(data) == 0:
                        print("Bug found: read zero bytes from pty master")
                        time.sleep(1)
                    else:
                        self.serial.write(data)
                except OSError as e:
                    if e.errno == 11:
                        #if self.verbose:
                        #    print('tack',end='',flush=True)
                        time.sleep(0.5)
                    else:
                        break
        except serial.SerialException:
            self.alive = False
            raise       # XXX handle instead of re-raise?
            
    def kbd(self):
        """loop and copy serial->uinput"""
        # for versoe output
        keystat=['UP','DOWN']
        # open uinput
        with evdev.UInput(name=self.kbd_name) as  ui:
            time.sleep(1) # wait for evdev.UInput() to settle
            try:
                # switch echo print off when typing
                if not self.echo:
                    self.serial.write(b'\x91')
                while self.alive:
                    # read all that is there or wait for one byte
                    if (self.serial.inWaiting() > 0):
                        data = self.serial.read()
                        if data:
                            # there is serial data
                            kbd_data=data[0]
                            if self.verbose:
                                print("erika:",hex(kbd_data),end='')
                            # realisiere Umschaltung durch Code bei einigen Tasten
                            if kbd_data==0xbb:
                                data = self.serial.read()
                                kbd_data=data[0]
                                if self.verbose:
                                    print("+",hex(kbd_data),end='',sep='')
                                kbd_data += 0x40
                            if e2i[kbd_data]:
                                # Jetzt ist die richtige Taste gefunden
                                if self.verbose:
                                    print(" =>",e2i[kbd_data][0],flush=True)
                                if len(e2i[kbd_data])>1:
                                    # there are keycodes defined
                                    key_lst=e2i[kbd_data][1]
                                    lenght=len(key_lst)
                                    i=0
                                    while i < lenght:
                                        # iterate over keycodes
                                        if self.verbose:
                                            print(e.KEY[key_lst[i]],keystat[key_lst[i+1]],sep='.',end=', ')
                                        ui.write(e.EV_KEY,key_lst[i],key_lst[i+1])
                                        i += 2
                                    ui.syn()
                                    if self.verbose:
                                        print(flush=True)
                                else:
                                    if self.verbose:
                                        print("NO KEYS",flush=True)
                            else:
                                # erika code not defined
                                print("Error",kbd_data,"unknown!",flush=True)
                    else:
                        # no serial data, just wait a bit
                        time.sleep(0.2)
                        # if self.verbose:
                        #    print('tick',end='',flush=True)
            except serial.SerialException:
                self.alive = False
                raise       # XXX handle instead of re-raise?