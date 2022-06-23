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

# from erika.erika2uinput import erika2uinput as e2i
import importlib

class Erika:
    def __init__(self, name, serdev, baudrate, rtscts, setperm, verbose, echo):
        self.serial          = serial.Serial()
        self.serial.port     = serdev
        self.serial.baudrate = baudrate
        self.serial.rtscts   = rtscts
        self.lpsetperm       = setperm
        # stats
        self.alive           = None
        self.threads         = []
        self.verbose         = verbose
        self.name            = name
        self.echo            = echo
        self.step            = 1

        # button state
        self.m_btn_left          = False
        self.m_btn_right         = False

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
        kbdcl = getattr(importlib.import_module('erika.erika2uinput'),'s3015')
        print(kbdcl.erika2uinput[0x4f])
        kbd=kbdcl()
        # for verbose output
        # keystat=['UP','DOWN']
        # define mouse capabilities
        # # have to use two input device, since I could not get a merged one going 
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
                # switch echo print off when typing
                if self.echo:
                    self.serial.write(b'\x92')
                else:
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
                            # warning this might block if there is no serial byte anymore
                            ######################
                            kbd.key(kbd_data)
                            ######################
                            # if kbd_data==0xbb:
                            #     data = self.serial.read()
                            #     kbd_data=data[0]
                            #     if self.verbose:
                            #         print("+",hex(kbd_data),end='',sep='')
                            #     kbd_data += 0x40
                            # if kbd.e2i[kbd_data]:
                            #     # Jetzt ist die richtige Taste gefunden
                            #     if self.verbose:
                            #         print(" =>",kbd.e2i[kbd_data][0],flush=True)
                            #     if len(kbd.e2i[kbd_data])>1:
                            #         # there are keycodes defined
                            #         if self.echo:
                            #             continue
                            #         key_lst=kbd.e2i[kbd_data][1]
                            #         lenght=len(key_lst)
                            #         i=0
                            #         while i < lenght:
                            #             # iterate over keycodes
                            #             if self.verbose:
                            #                 print(e.KEY[key_lst[i]],keystat[key_lst[i+1]],sep='.',end=', ')
                            #             ui.write(e.EV_KEY,key_lst[i],key_lst[i+1])
                            #             i += 2
                            #         ui.syn()
                            #         if self.verbose:
                            #             print(flush=True)
                            #     else:
                            #         # no keycodes defined, maybe a special key
                            #         if self.verbose:
                            #             print("NO KEYS - start xkey",flush=True)
                            #         self.xkey(kbd_data,mui)
                            # else:
                            #     # erika code not defined
                            #     print("Error",kbd_data,"unknown!",flush=True)
                            #########################
                    else:
                        # no serial data, just wait a bit
                        time.sleep(0.2)
                        # if self.verbose:
                        #    print('kbd-tick',end='',flush=True)
            except serial.SerialException:
                self.alive = False
                raise       # maybe serial device is removed

    # def xkey(self, kbd_data,mui):
    #     """decode special keys"""
    #     if kbd_data == 0xf4:
    #         # Mode T+
    #         if self.echo:
    #             self.echo = False
    #             self.serial.write(b'\x91')
    #         else:
    #             self.echo = True
    #             self.serial.write(b'\x92')
    #         if self.verbose:
    #             print("Echo",self.echo)
    #         return
    #     if self.echo:
    #         return
    #     if kbd_data == 0x83:
    #         # Form Feed
    #         if self.verbose:
    #             print("Form Feed")
    #         self.serial.write(b'\x83')
    #     if kbd_data == 0xfd:
    #         # MODE+Form Feed - Reset if next is y
    #         if self.verbose:
    #             print("Reset? (press y)")
    #         if b'\x51' == self.serial.read():
    #             if self.verbose:
    #                 print('shutdown -r now')
    #             os.system('shutdown -r now')
    #     # Mouse movement
    #     elif kbd_data ==0x7d:
    #         # Code T+ - adjust step
    #         if self.step == 1:
    #             self.step=8
    #         elif self.step == 8:
    #             self.step=32
    #         else:
    #             self.step=1
    #         if self.verbose:
    #             print("Mouse step:",self.step)
    #     elif kbd_data == 0xc5:
    #         # Mode W - Mouse up
    #         if self.verbose:
    #             print("Mouse up",self.step)
    #         mui.write(e.EV_REL,e.REL_Y,-1*self.step)
    #     elif kbd_data == 0xc6:
    #         # Mode S - Mouse down
    #         if self.verbose:
    #             print("Mouse down",self.step)
    #         mui.write(e.EV_REL,e.REL_Y,self.step)
    #     elif kbd_data == 0xc2:
    #         # Mode A - Mouse left
    #         if self.verbose:
    #             print("Mouse left",self.step)
    #         mui.write(e.EV_REL,e.REL_X,-1*self.step)
    #     elif kbd_data == 0xca:
    #         # Mode D - Mouse right
    #         if self.verbose:
    #             print("Mouse right",self.step)
    #         mui.write(e.EV_REL,e.REL_X,self.step)
    #     elif kbd_data == 0xc3:
    #         # Mode Y - Mouse BTN left
    #         if self.verbose:
    #             print("Mouse BTN left")
    #         self.m_btn_left=False
    #         mui.write(e.EV_KEY,e.BTN_LEFT,1)
    #         mui.write(e.EV_KEY,e.BTN_LEFT,0)
    #     elif kbd_data == 0xc7:
    #         # Mode X - Mouse BTN left - Switch
    #         if self.m_btn_left:
    #             self.m_btn_left=False
    #             mui.write(e.EV_KEY,e.BTN_LEFT,0)
    #         else:
    #             self.m_btn_left=True
    #             mui.write(e.EV_KEY,e.BTN_LEFT,1)
    #         if self.verbose:
    #             print("Mouse BTN left", self.m_btn_left)
    #     elif kbd_data == 0xcB:
    #         # Mode C - Mouse BTN right
    #         if self.verbose:
    #             print("Mouse BTN right")
    #         mui.write(e.EV_KEY,e.BTN_RIGHT,1)
    #         mui.write(e.EV_KEY,e.BTN_RIGHT,0)
    #     elif kbd_data == 0xcF:
    #         # Mode V - Mouse BTN right - Switch
    #         if self.m_btn_right:
    #             self.m_btn_right=False
    #             mui.write(e.EV_KEY,e.BTN_RIGHT,0)
    #         else:
    #             self.m_btn_right=True
    #             mui.write(e.EV_KEY,e.BTN_RIGHT,1)
    #         if self.verbose:
    #             print("Mouse BTN right", self.m_btn_right)
    #     mui.syn()
