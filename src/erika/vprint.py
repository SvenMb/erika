# -*- coding: utf-8 -*-
#

#  vprint.py
#  
#  Copyright 2022  <sven@muehlberg.net>
#  
#  

def init():
    global verbose
    verbose = 0

def inc():
    global verbose
    verbose += 1

# print verbose messages
def msg(lv,*args,**kwargs):
    global verbose
    if verbose >= lv:
        print(*args,**kwargs)
