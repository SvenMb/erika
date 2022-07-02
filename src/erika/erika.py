# -*- coding: utf-8 -*-
#

#  erika.py
#  
#  Copyright 2022  <sven@muehlberg.net>
#  
#  

import serial
import time

import threading,os,stat

import evdev
from evdev import ecodes as e
from courier_de import courier_de

import importlib


class Erika:
    def __init__(self, name, serdev, baudrate, rtscts, keyboard, setperm, verbose, echo):
        self.serial          = serial.Serial()
        self.serial.port     = serdev
        self.serial.baudrate = baudrate
        self.serial.rtscts   = rtscts
        self.lpsetperm       = setperm
        self.keyboard        = keyboard
        # stats
        self.alive           = None
        self.threads         = []
        self.verbose         = verbose
        self.name            = name
        self.echo            = echo
 
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

    ###########################
    
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

    ###########################
        
    def lp(self):
        """loop and copy pts->serial"""
        # create pts and print name (later link it"""
        master,vserial = os.openpty()
        vs_name = os.ttyname(vserial)
        if self.verbose:
            print("lp-device    :",vs_name)
        if not not self.lpsetperm: # not empty string
            if self.verbose:
                print("start setperm:",self.lpsetperm,vs_name)
            os.system(self.lpsetperm + " " + vs_name)
        with courier_de as cm:
            try:
                os.set_blocking(master,False)
                while self.alive:
                    try:
                        data = os.read(master,1)
                        if len(data) == 0:
                            print("Bug found: read zero bytes from pty master")
                            time.sleep(1)
                        else:
                            self.serial.write(cm.decode(data))
                    except OSError as e:
                        if e.errno == 11:
                            #if self.verbose:
                            #    print('lp-tick',end='',flush=True)
                            time.sleep(1)
                        else:
                            self.alive = False
                            break
            except serial.SerialException:
                self.alive = False
                raise       # maybe serial device is removed

    ###########################

    def kbd(self):
        """loop and copy serial->uinput"""

        # autodetect machine type
        if self.keyboard in ('de'):
            keyboard='unknown'
            # switch echo print off, this also starts infos from erika about stat and keys
            self.serial.write(b'\x91')
	        # read max 6 bytes or 0,6s wait
            for i in range(0,5):
                if (self.serial.inWaiting() > 0):
                    data = self.serial.read()
                    if self.verbose:
                        print("erikastart[",i,"]: ",hex(data[0]),sep='')
                    if data[0] in (0x84,0x85,0x86,0x87,0x88):
                        keyboard='3004'
                    elif data[0] in (0xf8,0xf9,0xfa,0xfe,0xff):
                        keyboard='3005'
                else:
                    time.sleep(0.1)
            self.keyboard=keyboard+'_'+self.keyboard
            # if self.verbose:
            print("Keyboard     :",self.keyboard,flush=True)

        if self.keyboard in ('3004_de','3005_de'):
            kbd = getattr(importlib.import_module('erika.s'+self.keyboard),'s'+self.keyboard)()
            # print(self.kbdcl.erika2uinput[0x4f])
        # elif self.keyboard != 'none':
        else:
            print('unknown keyboard!!!',flush=True)
            quit()

        # set echo on or off
        if self.echo:
            self.serial.write(b'\x92')
        else:
            self.serial.write(b'\x91')
 
        # define mouse capabilities
        # have to use two input device, since I could not get a merged one going 
        cap = {
         e.EV_REL : (e.REL_X, e.REL_Y),
         e.EV_KEY : (e.BTN_LEFT, e.BTN_MIDDLE, e.BTN_RIGHT),
        }
        # open uinput
        with evdev.UInput(name=self.name+' kbd') as  ui, evdev.UInput(cap,name=self.name+' mouse') as mui:
            time.sleep(1) # wait for evdev.UInput() to settle
            if self.verbose:
                print('Mouse cap:',mui.capabilities())
            kbd.init(ui, mui, self.serial, self.verbose, self.echo)
            try:
                while self.alive:
                    # read all that is there or wait for one byte
                    if (self.serial.inWaiting() > 0):
                        data = self.serial.read()
                        if data:
                            # there is serial data
                            kbd_data=data[0]
                            if self.verbose:
                                print("erika code:",hex(kbd_data))
                            kbd.key(kbd_data)
                    else:
                        # no serial data, just wait a bit
                        time.sleep(0.2)
                        # if self.verbose:
                        #    print('kbd-tick',end='',flush=True)
            except serial.SerialException:
                self.alive = False
                raise       # maybe serial device is removed
