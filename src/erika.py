#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  erika.py
#  
#  Copyright 2022  <sven@muehlberg.net>
#  
#  

from erika.erika import Erika
import sys, getopt


def main(argv):
    
    e = Erika()
    
    # comand line args
    try:
        opts, args = getopt.getopt(argv,"hved:b:k:p:i:s:l:c:",
            ["help","verbose","echo","device=","baudrate=","keyboard=",'wheel=','paper=','setperm=','cpi=','linespacing=','halflines=','columns='])
    except getopt.GetoptError:
        print('erika.py argument error')
        print('use erika.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('erika.py\n')
            print('USAGE:')
            print('\terika.py [OPTIONS]\n')
            print('OPTIONS:')
            print('\t-h, --help\t\tprint help information')
            print('\t-v, --verbose\t\tbe more verbose')
            print('\t\tcan be added multiple times to be even more verbose')
            print('\t-e, --echo\t\tconnect keyboard to typewriter')
            print('\t-d, --device <device>\tserial device to use')
            print('\t\tExample device name: /dev/ttyAMA0 or /dev/ttyUSB0')
            print('\t\tdefault: ', e.serial.port )
            print('\t-b, --baudrate <rate>\tbaudrate for erika')
            print('\t\terika manual says don\'t change!')
            print('\t\tExample baudrate: 1200')
            print('\t\tdefault: ', e.serial.baudrate )
            print('\t-k, --keyboard <map>\tkeyboard map to use')
            print('\t\tpossible keyboards: de, 3004_de, 3005_de, none')
            print('\t\tdefault: ', e.keyboard )
            print('\t\tuse \'de\' for autodetect machine type (only\n\t\timplemented language currently)')
            print('\t\tuse \'none\' if you don\'t want to use the erika\n\t\tkeyboard for input')
            print('\t\tcurrently implemented 3004_de and 3005_de.')
            print('\t\t3005, 3006, 3015, 3016 use the same keycodes.')
            print('\t-p, --setperm <script>\tscript to create link and set\n\t\tpermission for virtual lp-device')
            print('\t\tExample: sudo lp_setperm')
            print('\t\tdefault: ', e.lpsetperm )
            print('\t-i, --cpi\t\tcharacters per inch, char density')
            print('\t\tdefault: ', int(60/e.charstep))
            print('\t\tuse 10, 12 with normal daisy wheel, 15 possible on\n\t\t3005(and up) with special daisy wheel')
            print('\t-s, --linespacing\t\thalf lines used for one printed line')
            print('\t\tpossible spacing: 2, 3, 4')
            print('\t\tdefault: ',e.linestep)
            print('\t-l, --halflines\t\tmax half lines per paper sheet')
            print('\t\tdefault: ', e.maxlines)
            print('\t\tA4 - 120 half lines')
            print('\t-c, --columns\t\tmax half char per line')
            print('\t\tdefault: ', int(e.maxcolumns/e.charstep))
            print('\t\tA4 - 84 columns on 12 cpi')
            sys.exit()
        elif opt in ('-e','--echo'):
            e.echo = True
        elif opt in ('-d', '--device'):
            e.serial.port = arg
        elif opt in ('-b', '--baudrate'):
            e.serial.baudrate = arg
        elif opt in ('-k', '--keyboard'):
            e.keyboard = arg
        elif opt in ('-p', '--setperm'):
            e.lpsetperm = arg
        elif opt in ('-i', '--cpi'):
            if arg in ('10','12','15'):
                e.charstep=int(60/int(arg))
            else:
                print('wrong cpi',arg,'used.')
                sys.exit()
        elif opt in ('-s', '--linespacing'):
            if arg in ('2', '3', '4'):
                e.linestep=int(arg)
            else:
                print('wrong linespacing ',arg,' used.')
                sys.exit()
        elif opt in ('-l', '--halflines'):
            if arg.isnumeric():
                e.maxlines = int(arg)
            else:
                print('wrong halflines ',arg,' used.')
                sys.exit()
        elif opt in ('-c', '--columns'):
            if arg.isnumeric():
                e.maxcolumns = int(arg)*charstep
            else:
                print('wrong columns ',arg,' used.')
                sys.exit()
        elif opt in ('-v', '--verbose'):
            print('verbose arg:',arg)
            e.verbose+=1
            
    # info about current options         
    if e.verbose:
        print('Serial device:', e.serial.port)
        print('Baudrate     :', e.serial.baudrate)
        print('Keyboard     :', e.keyboard)
        print('lpsetperm prg:', e.lpsetperm)
        print('echo         :', e.echo)
        print('maxlines     :', e.maxlines)
        print('linestep     :', e.linestep)
        print('lines pp     :', int(e.maxlines/e.linestep))
        print('maxcolumns   :', e.maxcolumns)
        print('charstep     :', e.charstep)
        print('columns pl   :', int(e.maxcolumns/e.charstep))
        
    with e:
        e.alive=True
        if not (e.keyboard=='none'or e.keyboard==None):
            e.start_kbd()
        e.start_lp()
        # wait for threads
        for thread in e.threads:
             thread.join()

if __name__ == "__main__":
    main(sys.argv[1:])
    

