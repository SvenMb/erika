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
import erika.vprint as V

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
        self.backsteps       = 0

        self.alive           = None
        self.threads         = []
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

    # left border
    def firstCol(self,col=None):
        if not col:
            col = self.firstcol
        self.serial.write(b'\x8f') # open borders
        self.serial.write(b'\x78') # CR, maybe not needed
        # move back as far as possible
        for i in range(1,100):
            self.serial.write(b'\x72')
        for i in range(1,col):
            self.serial.write(b'\x71')
        self.serial.write(b'\x7e')
        V.msg(1,'first column set on erika to:',col)
        return col

    def lp(self):
        """loop and copy pts->serial"""
        # create pts and print name (later link it"""
        master,vserial = os.openpty()
        vs_name = os.ttyname(vserial)
        V.msg(1,"lp-device    :",vs_name)
        if not not self.lpsetperm: # not empty string
            V.msg(1,"start setperm:",self.lpsetperm,vs_name)
            os.system(self.lpsetperm + " " + vs_name)
        # wait for keyboard init ...
        time.sleep(2)
        # check if printer is detected
        if self.keyboard not in ('3004_de','3005_de'):
            self.alive = False
            V.msg (0,'unknown printer')
            quit()
        # check if keyboard init is aborted
        elif not self.alive:
            V.msg (0,'initialization aborted')
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

        firstcol = self.firstCol()

        with courier_de(self.charset) as cm:
            try:
                os.set_blocking(master,True)
                while self.alive:
                    # try:
                        data = os.read(master,1)
                        if len(data) == 0:
                            V.msg(0,"Bug found: read zero bytes from pty master")
                            time.sleep(1)
                        # check for escape, adapted from if6000
                        elif data == b'\x1b':
                            V.msg(1,"escape found")
                            data = os.read(master,1)
                            if   data == b'M':
                                V.msg(1,"ESC M -> 10cpi")
                                self.serial.write(b'\x87')
                                self.charstep=6
                            elif data == b'N':
                                V.msg(1,"ESC N -> 12cpi")
                                self.serial.write(b'\x88')
                                self.charstep=5
                            elif data == b'O':
                                V.msg(1,"ESC O -> 15cpi")
                                self.serial.write(b'\x89')
                                self.charstep=4
                            elif data == b'3':
                                V.msg(1,"ESC 3 -> 2 halflines spacing")
                                self.serial.write(b'\x84')
                                self.linestep=2
                            elif data == b'4':
                                V.msg(1,"ESC 4 -> 3 halflines spacing")
                                self.serial.write(b'\x85')
                                self.linestep=3
                            elif data == b'5':
                                V.msg(1,"ESC 5 -> 4 halflines spacing")
                                self.serial.write(b'\x86')
                                self.linestep=4
                            elif data == b'U':
                                V.msg(1,"ESC U -> halfline forward")
                                self.serial.write(b'\x75')
                                self.line+=1
                            elif data == b'D':
                                V.msg(1,"ESC D -> halfline backward")
                                self.serial.write(b'\x76')
                                self.line-=1
                            elif data == b'W':
                                V.msg(1,"ESC W -> LineWrap on")
                                self.wrap=True
                            elif data == b'w':
                                V.msg(1,"ESC w -> LineWrap off")
                                self.wrap=False
                            elif data == b'T':
                                V.msg(1,"ESC T -> tabstop: ",end='',flush=True)
                                data = os.read(master,1)
                                self.tabstop = data[0]
                                V.msg(1,self.tabstop,"spaces")
                            elif data == b'Z':
                                V.msg(1,"ESC Z -> charset utf-8/cp858")
                                cm.charset='cp858'
                            elif data == b'z':
                                V.msg(1,"ESC z -> charset IF6000/DIN66003")
                                cm.charset='if6000'
                            elif data == b'L':
                                V.msg(1,"ESC L -> max lines: ",end='',flush=True)
                                data = os.read(master,1)
                                self.maxlines = data[0]
                                V.msg(1,self.maxlines)
                            elif data == b'C':
                                V.msg(1,"ESC C -> max Columns: ",end='',flush=True)
                                data = os.read(master,1)
                                self.maxcolumns = data[0] * self.charstep - 1
                                V.msg(1,data[0])
                            elif data == b'F':
                                V.msg(1,"ESC F -> first Column: ",end='',flush=True)
                                data = os.read(master,1)
                                self.firstcol = data[0]
                                V.msg(1,data[0])
                            elif data == b'B':
                                V.msg(1,"ESC B -> Backsteps: ",end='',flush=True)
                                data = os.read(master,1)
                                self.backsteps = data[0]
                                V.msg(1,data[0])
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
                                V.msg(2,"line:",self.line)
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
                                V.msg (2,"space to next tabstop:",t)
                                while t > 0:
                                    self.serial.write(b'\x71')
                                    t-=1
                            # check for form feed
                            if data == b'\x0c' or self.line > self.maxlines:
                                # double beep
                                self.serial.write(b'\xaa\x10')
                                time.sleep(0.5)
                                self.serial.write(b'\xaa\x10')
                                self.kbd_wait=True
                                V.msg(0,"Form Feed, waiting for kbd")
                                # waiting for kbd thread to message
                                while self.kbd_wait:
                                    time.sleep(0.5)
                                self.serial.write(b'\xaa\x20')
                                # formfeed done, do backsteps
                                for i in range(0,self.backsteps):
                                    self.serial.write(b'\x76')
                                    V.msg(1,"Backstep...")
                                    # if formfeed, then also carriage return
                                if data == b'\x0c':
                                    data = b'\r'
                                # reset line counter
                                self.line=0
                                self.column=0
                            # don't print if outside border
                            if self.column > self.maxcolumns:
                                continue
                            erika_char=cm.decode(data)
                            # every printable char
                            if data not in (b'\b',b'\n',b'\r',b'\x0c') and erika_char:
                                self.column += self.charstep
                                V.msg(2,'column:',self.column,flush=True)

                            # write the char to serial in erika code
                            self.serial.write(erika_char)

                            # adjust rand again if needed and last char was \n or \r
                            if data in (b'\n',b'\r') and firstcol !=self.firstcol:
                                firstcol = self.firstCol()

                    # except OSError as e:
                    #    if e.errno == 11:
                    #        if self.verbose >2 :
                    #            print('lp-tick',end='',flush=True)
                    #        time.sleep(1)
                    #    else:
                    #        self.alive = False
                    #        break
            #except serial.SerialException:
            except:
                self.alive = False
                V.msg(0,"lp-thread stopped!",flush=True)
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
                    V.msg(1,"erikastart[",i,"]: ",hex(data[0]),sep='')
                    if data[0] in (0x84,0x85,0x86,0x87,0x88):
                        keyboard='3004'
                    elif data[0] in (0xf8,0xf9,0xfa,0xfe,0xff):
                        keyboard='3005'
                else:
                    time.sleep(0.1)
            self.keyboard=keyboard+'_'+self.keyboard
            V.msg(0,"Keyboard     :",self.keyboard,flush=True)

        if self.keyboard in ('3004_de','3005_de'):
            kbd = getattr(importlib.import_module('erika.s'+self.keyboard),'s'+self.keyboard)()
            # print(self.kbdcl.erika2uinput[0x4f])
        # elif self.keyboard != 'none':
        else:
            self.alive = False
            V.msg(0,'unknown keyboard!!!',flush=True)
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
        try:
            with evdev.UInput(name=self.name+' kbd') as  ui, evdev.UInput(cap,name=self.name+' mouse') as mui:
                time.sleep(1) # wait for evdev.UInput() to settle
                V.msg(2,'Mouse cap:',mui.capabilities())
                kbd.init(ui, mui, self.serial, self.echo)
                while self.alive:
                    # read all that is there or wait for one byte
                    if (self.serial.inWaiting() > 0):
                        data = self.serial.read()
                        if data:
                            # there is serial data
                            kbd_data=data[0]
                            V.msg(2,"erika code:",hex(kbd_data))
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
                        if kbd.alttab>0:
                            kbd.alttab-=1
                            # release ALT-key when self.alttab reached 0
                            if kbd.alttab==0:
                                ui.write(e.EV_KEY,e.KEY_LEFTALT,0)
                                ui.syn()
                                V.msg(2,'ALT-TAB-Timeout')
                        V.msg(3,'kbd-tick',end='',flush=True)
        except:
            self.alive = False
            raise       # maybe serial device is removed
 
