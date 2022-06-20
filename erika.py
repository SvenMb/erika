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
    # Defaults for raspberry and erika 3004
    serdev='/dev/ttyAMA0'
    baudrate=1200
    rtscts=True
    keyboard='erika3004_de'
    wheel='german_courier'
    lpsetperm='sudo ./setperm.sh'
    verbose=False
    
    # load from config file... not implemented yet
    
    # comand line args
    try:
        opts, args = getopt.getopt(argv,"hvd:b:k:w:p:s:",["help=","verbose=","device=","baudrate=","keyboard=",'wheel=','paper=','setperm='])
    except getopt.GetoptError:
        print('erika.py argument error')
        print('use erika.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('erika.py\n')
            print('USAGE:')
            print('\terika.py [OPTIONS]\n')
            print('OPTIONS:')
            print('\t-h, --help\t\tprint help information')
            print('\t-v, --verbose\t\tbe more verbose')
            print('\t-d, --device <device>\tserial device to use')
            print('\t\tExample device name: /dev/ttyAMA0 or /dev/ttyUSB0')
            print('\t\tdefault: ', serdev )
            print('\t-b, --baudrate <rate>\tbaudrate for erika')
            print('\t\tExample baudrate: 1200')
            print('\t\tdefault: ', baudrate )
            print('\t-k, --keyboard <map>\tkeyboard map to use')
            print('\t\tpossible keyboards: erika3004_de, erika3006_de, erika3015_de, none')
            print('\t\tuse \'none\' if you don\'t want to use the erika keyboard for input')
            print('\t\tdefault: ', keyboard )
            print('\t-w, --wheel <wheel>\ttypewriter daisy (font) wheel to use')
            print('\t\tpossible wheels: german_courier')
            print('\t\tdefault: ', wheel )
            print('\t-s, --setperm <script>\tscript to create link and set permission for virtual lp-device')
            print('\t\tExample: sudo lp_setperm')
            print('\t\tdefault: ', lpsetperm )
            sys.exit()
        elif opt in ('-d', '--device'):
            serdev = arg
        elif opt in ('-b', '--baudrate'):
            baudrate = arg
        elif opt in ('-k', '--keyboard'):
            keyboard = arg
        elif opt in ('-w', '--wheel'):
            wheel = arg
        elif opt in ('-s', '--setperm'):
            lpsetperm = arg
        elif opt == '-v':
            verbose=True
            
    # info about current options         
    if verbose:
        print('Serial device:', serdev)
        print('Baudrate     :', baudrate)
        print('Keyboard     :', keyboard)
        print('Daisy wheel  :', wheel)
        print('lpsetperm prg:', lpsetperm)
        
    # initialise hardware parameter
    e = Erika(serdev, baudrate, rtscts,lpsetperm,verbose)
    with e:
        # e.write("Hallo, ich drucke!\r\n".encode('ascii'))
        e.alive=True
        if not (keyboard=='none'or keyboard==None):
            e.start_kbd()
        e.start_lp()
        # wait for threads
        for thread in e.threads:
             thread.join()

if __name__ == "__main__":
    main(sys.argv[1:])
    

