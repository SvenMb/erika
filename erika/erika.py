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
        # thread gets kiled when programs exit 
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
                        if self.verbose:
                            print('tack',end='',flush=True)
                        time.sleep(0.5)
                    else:
                        break
        except serial.SerialException:
            self.alive = False
            raise       # XXX handle instead of re-raise?
            
    def kbd(self):
        """loop and copy serial->uinput"""
        try:
            while self.alive:
                # read all that is there or wait for one byte
                if (self.serial.inWaiting() > 0):
                    data = self.serial.read()
                    if data:
                        if data == b'q':
                            if self.verbose:
                                print("\nquit")
                            self.alive=False
                        elif data == b'a':
                            self.serial.write("A gedrueckt!\r\n".encode('utf-8'))
                        else:
                            print(chr(data[0]),end='',flush=True)
                else:
                    time.sleep(0.2)
                    if self.verbose:
                        print('tick',end='',flush=True)
        except serial.SerialException:
            self.alive = False
            raise       # XXX handle instead of re-raise?
    