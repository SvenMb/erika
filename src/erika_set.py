#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  erika_set.py
#  
#  Copyright 2022  <sven@muehlberg.net>
#  
#  

import serial
import os, sys, getopt

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main(argv):

    s          = serial.Serial()
    s.port     = '/dev/erika/erika'
    
    verbose    = 0
    cpi        = None
    linestep   = None
    maxlines   = None
    maxcolumns = None
    tabstop    = None
    charset    = None
    firstcol   = None
    
    # comand line args
    try:
        opts, args = getopt.getopt(argv,"hvd:i:s:l:c:f:t:z:",
            ["help","verbose","device=","cpi=","linespacing=","tabstop="])
    except getopt.GetoptError:
        eprint('erika.py argument error')
        eprint('use erika_set.py -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('erika_set.py\n')
            print('USAGE:')
            print('\terika_set.py [OPTIONS]\n')
            print('OPTIONS:')
            print('\t-h, --help\t\tprint help information')
            print('\t-v, --verbose\t\tbe more verbose')
            print('\t\tcan be added multiple times to be even more verbose')
            print('\t-d, --device <device>\tserial device to use')
            print('\t\tdefault: ', s.port )
            print('\t\tif \'-\' is given as devicename, stdout is used')
            print('\t-i, --cpi\t\tcharacters per inch, char density')
            print('\t\tuse 10, 12 with normal daisy wheel, 15 possible on\n\t\t3005(and up) with special daisy wheel')
            print('\t-s, --linespacing\t\thalf lines used for one printed line')
            print('\t\tpossible spacing: 2, 3, 4')
            print('\t-l, --halflines\t\tmax half lines per paper sheet')
            print('\t\tA4 - 120 half lines')
            print('\t-c, --columns\t\tmax half char per line')
            print('\t\trecommended:')
            print('\t\tA4 - 84 columns on 12 cpi')
            print('\t\tmax 150 columns')
            print('\t-f, --firstcolumn\t\tfirst column')
            print('\t\trecommended 10 for 10cpi, 12 for 12cpi and 15 for 15cpi')
            print('\t\tstarting with 1')
            print('\t-t, --tabstop\t\tdistance tabstops')
            print('\t\trecommended 4 or 8')
            print('\t-z, --charset\t\textra charset (Zeichenkodierung)')
            print('\t\tselectable from cp858 and if6000')
            print('\t\tmain charset is always utf-8')
            sys.exit()
        elif opt in ('-d', '--device'):
            s.port = arg
        elif opt in ('-v', '--verbose'):
            verbose += 1
        elif opt in ('-i', '--cpi'):
            if arg in ('10','12','15'):
                cpi = arg
            else:
                eprint('ERROR: Wrong cpi:', arg)
                eprint('ERROR: only 10, 12 or 15 possible')
                sys.exit(2)
        elif opt in ('-s', '--linespacing'):
            if arg in ('2', '3', '4'):
                linestep=arg
            else:
                eprint('ERROR: wrong linespacing:',arg)
                eprint('ERROR: only 2, 3 or 4 possible')
                sys.exit(2)
        elif opt in ('-l', '--halflines'):
            if arg.isnumeric() and int(arg) < 256:
                maxlines = int(arg)
            else:
                eprint('ERROR: wrong halflines ',arg,' used.')
                sys.exit(2)
        elif opt in ('-c', '--columns'):
            if arg.isnumeric() and int(arg) < 151:
                maxcolumns = int(arg)
            else:
                eprint('ERROR: wrong columns ',arg,' used.')
                sys.exit(2)
        elif opt in ('-f','--firstcolumn'):
            if arg.isnumeric() and int(arg) > 0:
                firstcol = int(arg)
            else:
                eprint('ERROR: wrong firstcolumn',arg)
                sys.exit(2)
        elif opt in ('-t', '--tabstop'):
            if arg in ('4','8'):
                tabstop = arg
            else:
                eprint('ERROR: wrong tabstop:',arg)
                eprint('ERROR: only 4 or 8 possible here, use erika daemon setting for other values')
                sys.exit(2)
        elif opt in ('-z', '--charset'):
            if arg in ('cp858','if6000'):
                charset = arg
            else:
                eprint('ERROR: wrong extra charset',arg)
                sys.exit(2)



    # info about current options         
    if verbose:
        eprint('DEBUG: Erika device:', s.port)
        eprint('DEBUG: verbose      :',verbose)
        if cpi:
            eprint('DEBUG: cpi          :', cpi)
        if maxcolumns:
            eprint('DEBUG: maxcolumns   :', maxcolumns)
        if linestep:
            eprint('DEBUG: linestep     :', linestep)
        if maxlines:
            eprint('DEBUG: maxlines     :', maxlines)
        if firstcol:
            eprint('DEBUG: firstcolumn  :', firstcol)
        if tabstop:
            eprint('DEBUG: tabstop      :', tabstop)
        if charset:
            eprint('DEBUG: extra charset:', charset)

    # open erika port
    if s.port != '-':
        try:
            s.open()
        except serial.SerialException as e:
            eprint(e)
            eprint('CRIT: erika daemon not running or wrong device name')
            eprint('CRIT: use erika_set.py -h for help')
            sys.exit(2)
    # or stdout
    else:
        s = os.fdopen(sys.stdout.fileno(), 'wb',closefd=False)
    # cpi
    if cpi:
        if cpi == '15':
            s.write(b'\x1bO')
        elif cpi == '12':
            s.write(b'\x1bN')
        else: # should be 10 now
            s.write(b'\x1bM')
        eprint('INFO: cpi set to        :', cpi)

    # linespacing
    if linestep:
        if linestep == '2':
            s.write(b'\x1b3')
        elif linestep == '3':
            s.write(b'\x1b4')
        else: # should be 4 now
            s.write(b'\x1b5')
        eprint('INFO: linespacing set to:', linestep)

    # maxlines
    if maxlines:
        s.write(b'\x1bL' + maxlines.to_bytes(1,'big'))
        eprint('INFO: maxlines set to:', maxlines)

    # maxcolumns
    if maxcolumns:
        s.write(b'\x1bC' + maxcolumns.to_bytes(1,'big'))
        eprint('INFO: maxcolumns set to:', maxcolumns)

    # firstcolumn
    if firstcol:
        s.write(b'\x1bF' + firstcol.to_bytes(1,'big'))
        eprint('INFO: firstcolumn set to:', firstcol)
    
    # tabstop
    if tabstop:
        if tabstop == '4':
            s.write(b'\x1bT')
        else: # should be 8
            s.write(b'\x1bt')
        eprint('INFO: tabstop set to:', tabstop)

    # charset
    if charset:
        if charset == 'cp858':
            s.write(b'\x1bZ')
        else: # should be if6000
            s.write(b'\x1bz')
        eprint('INFO: charset set to:', charset)
    
    # s.write(b'    ')
    
if __name__ == "__main__":
    main(sys.argv[1:])
