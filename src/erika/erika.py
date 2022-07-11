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
from erika.courier_de import courier_de

import importlib


class Erika:
    def __init__(self):
        self.serial          = serial.Serial()
        # defaults
        self.serial.port     = '/dev/ttyAMA0'
        self.serial.baudrate = 1200
        self.serial.rtscts   = True
        self.lpsetperm       = './setperm.sh'
        self.keyboard        = 'de'
        self.linestep        = 2
        self.maxlines        = 120  # halflines per paper, 120 for normal A4
        self.maxcolumns      = 80*5 - 1 # chars per line
        self.charstep        = 5    # 4 => 15 cpi, 5 => 12 cpi, 6 => 10 cpi
        self.tabstop         = 8
        self.charset         = 'cp858'
        self.firstcol        = 12
        self.wrap            = False

        self.alive           = None
        self.threads         = []
        self.verbose         = 0
        self.name            = 'Erika 0.2'
        self.echo            = False
        self.kbd_wait        = False
        self.line            = 0 # half lines
        self.column          = 0 # 1/60 inch
 
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
        # wait for keyboard init ...
        time.sleep(2)
        # reset typewriter
        # self.serial.write(b'\x95')

        # set cpi
        if self.charstep == 4:   # 15 cpi
            self.serial.write(b'\x89')
        elif self.charstep == 5: # 12 cpi
            self.serial.write(b'\x88')
        else:                    # 10 cpi
            self.serial.write(b'\x87')

        # set linestep
        if self.linestep == 4:   # 2 lines spacing
            self.serial.write(b'\x86')
        elif self.linestep == 3: # 1.5 lines spacing
            self.serial.write(b'\x85')
        else:                      # 1 line spacing
            self.serial.write(b'\x84')

        # set firstcolumn
        for i in range(1,100):
            self.serial.write(b'\x72')
        for i in range(1,self.firstcol):
            self.serial.write(b'\x71')
        self.serial.write(b'\x7e')
        firstcol = self.firstcol

        with courier_de(self.charset) as cm:
            try:
                os.set_blocking(master,True)
                while self.alive:
                    try:
                        data = os.read(master,1)
                        if len(data) == 0:
                            print("Bug found: read zero bytes from pty master")
                            time.sleep(1)
                        else:
                            # check for escape, adapted from if6000
                            if data == b'\x1b':
                                print("escape found")
                                data = os.read(master,1)
                                if   data == b'M':
                                    if self.verbose:
                                        print("ESC M -> 10cpi")
                                    self.serial.write(b'\x87')
                                    self.charstep=6
                                elif data == b'N':
                                    if self.verbose:
                                        print("ESC N -> 12cpi")
                                    self.serial.write(b'\x88')
                                    self.charstep=5
                                elif data == b'O':
                                    if self.verbose:
                                        print("ESC O -> 15cpi")
                                    self.serial.write(b'\x89')
                                    self.charstep=4
                                elif data == b'3':
                                    if self.verbose:
                                        print("ESC 3 -> 2 halflines spacing")
                                    self.serial.write(b'\x84')
                                    self.linestep=2
                                elif data == b'4':
                                    if self.verbose:
                                        print("ESC 4 -> 3 halflines spacing")
                                    self.serial.write(b'\x85')
                                    self.linestep=3
                                elif data == b'5':
                                    if self.verbose:
                                        print("ESC 5 -> 4 halflines spacing")
                                    self.serial.write(b'\x86')
                                    self.linestep=4
                                elif data == b'U':
                                    if self.verbose:
                                        print("ESC U -> halfline forward")
                                    self.serial.write(b'\x75')
                                    self.line+=1
                                elif data == b'D':
                                    if self.verbose:
                                        print("ESC D -> halfline backward")
                                    self.serial.write(b'\x76')
                                    self.line-=1
                                elif data == b'W':
                                    if self.verbose:
                                        print("ESC W -> LineWrap on")
                                    self.wrap=True
                                elif data == b'w':
                                    if self.verbose:
                                        print("ESC w -> LineWrap off")
                                    self.wrap=False
                                elif data == b'T':
                                    if self.verbose:
                                        print("ESC T -> tabstop: ",end='',flush=True)
                                    data = os.read(master,1)
                                    self.tabstop = data[0]
                                    if self.verbose:
                                        print(self.tabstop,"spaces")
                                elif data == b'Z':
                                    if self.verbose:
                                        print("ESC Z -> charset utf-8/cp858")
                                    cm.charset='cp858'
                                elif data == b'z':
                                    if self.verbose:
                                        print("ESC z -> charset IF6000/DIN66003")
                                    cm.charset='if6000'
                                elif data == b'L':
                                    if self.verbose:
                                        print("ESC L -> max lines: ",end='',flush=True)
                                    data = os.read(master,1)
                                    self.maxlines = data[0]
                                    if self.verbose:
                                        print(self.maxlines)
                                elif data == b'C':
                                    if self.verbose:
                                        print("ESC C -> max Columns: ",end='',flush=True)
                                    data = os.read(master,1)
                                    self.maxcolumns = data[0] * self.charstep - 1
                                    if self.verbose:
                                        print(data[0])
                                elif data == b'F':
                                    if self.verbose:
                                        print("ESC F -> first Column: ",end='',flush=True)
                                    data = os.read(master,1)
                                    self.firstcol = data[0]
                                    if self.verbose:
                                        print(data[0])
                                        
                            else:
                                # backstep, shouldn't happen to often, handle anyway
                                if data == b'\b':
                                    self.column -= self.charstep
                                    if self.column < 0:
                                       self.column = 0 
                                # check for newline or line overflow with wrap
                                elif data == b'\n' or (self.wrap and (self.column > self.maxcolumns)):
                                    self.line+=self.linestep
                                    self.column=0
                                    if self.verbose > 1:
                                        print("line:",self.line)
                                    if not data == b'\n':
                                        self.serial.write(b'\x77') # maybe already to far of paper, but we won't write here
                                # only carriage return
                                elif data == b'\r':
                                    self.column = 0
                                # tabs
                                elif data == b'\t':
                                    t = int(self.tabstop-(self.column/self.charstep)%self.tabstop)
                                    self.column+=self.charstep*t
                                    if self.column > self.maxcolumns:
                                        self.column = self.maxcolumns + self.charstep
                                    if self.verbose > 1:
                                        print ("space to next tabstop:",t)
                                    while t > 0:
                                        self.serial.write(b'\x71')
                                        t-=1
                                # check for form feed
                                if data == b'\x0c' or self.line > self.maxlines:
                                    # double beep
                                    self.serial.write(b'\xaa\x10')
                                    time.sleep(0.5)
                                    self.serial.write(b'\xaa\x10')
                                    # connect typewriter with keyboard
                                    # self.serial.write(b'\x92')
                                    # tell kb thread to wait
                                    self.kbd_wait=True
                                    if self.verbose:
                                        print("Form Feed, waiting for kbd")
                                    # waiting for kbd thread to message "Randloesen"
                                    while self.kbd_wait:
                                        time.sleep(0.5)
                                    # disconnect typewriter keyboard if wanted
                                    # if not self.echo:
                                    #    self.serial.write(b'\x91')
                                    self.serial.write(b'\xaa\x20')
                                    # if formfeed, then also carriage return
                                    if data == b'\x0c':
                                        data = b'\r'
                                    # reset line counter
                                    self.line=0
                                    self.column=0
                                # don't print if outside border
                                if self.column > self.maxcolumns:
                                    continue
                                # every printable char
                                if data not in (b'\b',b'\n',b'\r',b'\x0c'):
                                    self.column += self.charstep
                                    if self.verbose > 1:
                                        print('column:',self.column,flush=True)

                                self.serial.write(cm.decode(data))

                                # adjust rand again if needed and last char was \n or \r
                                if data in (b'\n',b'\r') and firstcol !=self.firstcol:
                                    # set firstcolumn
                                    for i in range(1,firstcol+10):
                                        self.serial.write(b'\x72')
                                    for i in range(1,self.firstcol):
                                        self.serial.write(b'\x71')
                                    self.serial.write(b'\x7e')
                                    firstcol = self.firstcol
                                    if self.verbose:
                                        print('first column set on erika to:',firstcol)

                    except OSError as e:
                        if e.errno == 11:
                            if self.verbose >2 :
                                print('lp-tick',end='',flush=True)
                            time.sleep(1)
                        else:
                            self.alive = False
                            break
            except serial.SerialException:
                self.alive = False
                if self.verbose:
                    print("lp-thread stopped!",flush=True)
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
                    if self.verbose > 1:
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
            if self.verbose > 1:
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
                            if self.verbose > 1:
                                print("erika code:",hex(kbd_data))
                            if self.kbd_wait:
                                if kbd_data in (0x75,0x76,0x77,0x81,0x82,0x83) and not self.echo:
                                    self.serial.write(data)
                                elif kbd_data in (0x80,0x71):
                                    self.kbd_wait=False
                            else:
                                kbd.key(kbd_data)
                    else:
                        # no serial data, just wait a bit
                        time.sleep(0.2)
                        if self.verbose > 2:
                            print('kbd-tick',end='',flush=True)
            except serial.SerialException:
                self.alive = False
                raise       # maybe serial device is removed
