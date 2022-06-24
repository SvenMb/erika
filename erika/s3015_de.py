# -*- coding: utf-8 -*-
#

#  erika.py
#  
#  Copyright 2022  <sven@muehlberg.net>
#  
#  

import os
from evdev import ecodes as e

class s3015_de:
    def init(self, ui, mui, serial, verbose, echo):
        self.ui      = ui
        self.mui     = mui
        self.serial  = serial
        self.verbose = verbose
        self.echo    = echo
        self.step    = 1

    # array for erika code to label and list of keycodes 0x00-0xFF) are for native erika codes
    # from 256 (0x100-0x12A) is for 0xbb excaped codes -0xC0, these are done with code key on
    # that typewriter  
    erika2uinput = [
        # 00
        None,
        ['_',[e.KEY_LEFTSHIFT,1,e.KEY_SLASH,1,e.KEY_SLASH,0,e.KEY_LEFTSHIFT,0]],
        ['&',[e.KEY_LEFTSHIFT,1,e.KEY_6,1,e.KEY_6,0,e.KEY_LEFTSHIFT,0]],
        ['" (no step)',[e.KEY_RIGHTALT,1,e.KEY_LEFTBRACE,1,e.KEY_LEFTBRACE,0,e.KEY_RIGHTALT,0]],
        ['%',[e.KEY_LEFTSHIFT,1,e.KEY_5,1,e.KEY_5,0,e.KEY_LEFTSHIFT,0]],
        ['i',[e.KEY_I,1,e.KEY_I,0]],
        ['£',[e.KEY_RIGHTALT,1,e.KEY_LEFTSHIFT,1,e.KEY_3,1,e.KEY_3,0,e.KEY_LEFTSHIFT,0,e.KEY_RIGHTALT,0]],
        ['µ',[e.KEY_RIGHTALT,1,e.KEY_M,1,e.KEY_M,0,e.KEY_RIGHTALT,0]],
        ['9',[e.KEY_9,1,e.KEY_9,0]],
        ['8',[e.KEY_8,1,e.KEY_8,0]],
        ['7',[e.KEY_7,1,e.KEY_7,0]],
        ['6',[e.KEY_6,1,e.KEY_6,0]],
        ['5',[e.KEY_5,1,e.KEY_5,0]],
        ['0',[e.KEY_0,1,e.KEY_0,0]],
        ['4',[e.KEY_4,1,e.KEY_4,0]],
        ['3',[e.KEY_3,1,e.KEY_3,0]],
        # 10
        ['2',[e.KEY_2,1,e.KEY_2,0]],
        ['1',[e.KEY_1,1,e.KEY_1,0]],
        ['H',[e.KEY_LEFTSHIFT,1,e.KEY_H,1,e.KEY_H,0,e.KEY_LEFTSHIFT,0]],
        [':',[e.KEY_LEFTSHIFT,1,e.KEY_DOT,1,e.KEY_DOT,0,e.KEY_LEFTSHIFT,0]],
        ['D',[e.KEY_LEFTSHIFT,1,e.KEY_D,1,e.KEY_D,0,e.KEY_LEFTSHIFT,0]],
        ['²',[e.KEY_RIGHTALT,1,e.KEY_2,1,e.KEY_2,0,e.KEY_RIGHTALT,0]],
        ['M',[e.KEY_LEFTSHIFT,1,e.KEY_M,1,e.KEY_M,0,e.KEY_LEFTSHIFT,0]],
        ['\'',[e.KEY_LEFTSHIFT,1,e.KEY_BACKSLASH,1,e.KEY_BACKSLASH,0,e.KEY_LEFTSHIFT,0]],
        ['B',[e.KEY_LEFTSHIFT,1,e.KEY_B,1,e.KEY_B,0,e.KEY_LEFTSHIFT,0]],
        ['^ (no step)',[e.KEY_GRAVE,1,e.KEY_GRAVE,0]],
        ['Q',[e.KEY_LEFTSHIFT,1,e.KEY_Q,1,e.KEY_Q,0,e.KEY_LEFTSHIFT,0]],
        ['*',[e.KEY_LEFTSHIFT,1,e.KEY_RIGHTBRACE,1,e.KEY_RIGHTBRACE,0,e.KEY_LEFTSHIFT,0]],
        ['G',[e.KEY_LEFTSHIFT,1,e.KEY_G,1,e.KEY_G,0,e.KEY_LEFTSHIFT,0]],
        ['(',[e.KEY_LEFTSHIFT,1,e.KEY_8,1,e.KEY_8,0,e.KEY_LEFTSHIFT,0]],
        ['O',[e.KEY_LEFTSHIFT,1,e.KEY_O,1,e.KEY_O,0,e.KEY_LEFTSHIFT,0]],
        [')',[e.KEY_LEFTSHIFT,1,e.KEY_9,1,e.KEY_9,0,e.KEY_LEFTSHIFT,0]],
        # 20
        ['C',[e.KEY_LEFTSHIFT,1,e.KEY_C,1,e.KEY_C,0,e.KEY_LEFTSHIFT,0]],
        ['I',[e.KEY_LEFTSHIFT,1,e.KEY_I,1,e.KEY_I,0,e.KEY_LEFTSHIFT,0]],
        ['V',[e.KEY_LEFTSHIFT,1,e.KEY_V,1,e.KEY_V,0,e.KEY_LEFTSHIFT,0]],
        ['³',[e.KEY_RIGHTALT,1,e.KEY_3,1,e.KEY_3,0,e.KEY_RIGHTALT,0]],
        ['K',[e.KEY_LEFTSHIFT,1,e.KEY_K,1,e.KEY_K,0,e.KEY_LEFTSHIFT,0]],
        ['+',[e.KEY_RIGHTBRACE,1,e.KEY_RIGHTBRACE,0]],
        ['X',[e.KEY_LEFTSHIFT,1,e.KEY_X,1,e.KEY_X,0,e.KEY_LEFTSHIFT,0]],
        ['|',[e.KEY_RIGHTALT,1,e.KEY_102ND,1,e.KEY_102ND,0,e.KEY_RIGHTALT,0]],
        ['U',[e.KEY_LEFTSHIFT,1,e.KEY_U,1,e.KEY_U,0,e.KEY_LEFTSHIFT,0]],
        ['´ (no step)',[e.KEY_EQUAL,1,e.KEY_EQUAL,0]],
        ['N',[e.KEY_LEFTSHIFT,1,e.KEY_N,1,e.KEY_N,0,e.KEY_LEFTSHIFT,0]],
        ['`',[e.KEY_LEFTSHIFT,1,e.KEY_EQUAL,1,e.KEY_EQUAL,0,e.KEY_LEFTSHIFT,0]],
        ['L',[e.KEY_LEFTSHIFT,1,e.KEY_L,1,e.KEY_L,0,e.KEY_LEFTSHIFT,0]],
        ['W',[e.KEY_LEFTSHIFT,1,e.KEY_W,1,e.KEY_W,0,e.KEY_LEFTSHIFT,0]],
        ['=',[e.KEY_LEFTSHIFT,1,e.KEY_0,1,e.KEY_0,0,e.KEY_LEFTSHIFT,0]],
        ['P',[e.KEY_LEFTSHIFT,1,e.KEY_P,1,e.KEY_P,0,e.KEY_LEFTSHIFT,0]],
        # 30
        ['A',[e.KEY_LEFTSHIFT,1,e.KEY_A,1,e.KEY_A,0,e.KEY_LEFTSHIFT,0]],
        ['Y',[e.KEY_LEFTSHIFT,1,e.KEY_Z,1,e.KEY_Z,0,e.KEY_LEFTSHIFT,0]],
        ['J',[e.KEY_LEFTSHIFT,1,e.KEY_J,1,e.KEY_J,0,e.KEY_LEFTSHIFT,0]],
        ['S',[e.KEY_LEFTSHIFT,1,e.KEY_S,1,e.KEY_S,0,e.KEY_LEFTSHIFT,0]],
        ['E',[e.KEY_LEFTSHIFT,1,e.KEY_E,1,e.KEY_E,0,e.KEY_LEFTSHIFT,0]],
        ['?',[e.KEY_LEFTSHIFT,1,e.KEY_MINUS,1,e.KEY_MINUS,0,e.KEY_LEFTSHIFT,0]],
        ['R',[e.KEY_LEFTSHIFT,1,e.KEY_R,1,e.KEY_R,0,e.KEY_LEFTSHIFT,0]],
        ['T',[e.KEY_LEFTSHIFT,1,e.KEY_T,1,e.KEY_T,0,e.KEY_LEFTSHIFT,0]],
        ['Z',[e.KEY_LEFTSHIFT,1,e.KEY_Y,1,e.KEY_Y,0,e.KEY_LEFTSHIFT,0]],
        ['°',[e.KEY_LEFTSHIFT,1,e.KEY_GRAVE,1,e.KEY_GRAVE,0,e.KEY_LEFTSHIFT,0]],
        ['Ü',[e.KEY_LEFTSHIFT,1,e.KEY_LEFTBRACE,1,e.KEY_LEFTBRACE,0,e.KEY_LEFTSHIFT,0]],
        [';',[e.KEY_LEFTSHIFT,1,e.KEY_COMMA,1,e.KEY_COMMA,0,e.KEY_LEFTSHIFT,0]],
        ['Ö',[e.KEY_LEFTSHIFT,1,e.KEY_SEMICOLON,1,e.KEY_SEMICOLON,0,e.KEY_LEFTSHIFT,0]],
        ['§',[e.KEY_LEFTSHIFT,1,e.KEY_3,1,e.KEY_3,0,e.KEY_LEFTSHIFT,0]],
        ['F',[e.KEY_LEFTSHIFT,1,e.KEY_F,1,e.KEY_F,0,e.KEY_LEFTSHIFT,0]],
        ['Ä',[e.KEY_LEFTSHIFT,1,e.KEY_APOSTROPHE,1,e.KEY_APOSTROPHE,0,e.KEY_LEFTSHIFT,0]],
        # 40
        ['/',[e.KEY_LEFTSHIFT,1,e.KEY_7,1,e.KEY_7,0,e.KEY_LEFTSHIFT,0]],
        ['#',[e.KEY_BACKSLASH,1,e.KEY_BACKSLASH,0]],
        ['!',[e.KEY_LEFTSHIFT,1,e.KEY_1,1,e.KEY_1,0,e.KEY_LEFTSHIFT,0]],
        ['"',[e.KEY_LEFTSHIFT,1,e.KEY_2,1,e.KEY_2,0,e.KEY_LEFTSHIFT,0]],
        ['é',[e.KEY_EQUAL,1,e.KEY_EQUAL,0,e.KEY_E,1,e.KEY_E,0]],
        ['ç',[e.KEY_RIGHTALT,1,e.KEY_EQUAL,1,e.KEY_EQUAL,0,e.KEY_RIGHTALT,0,e.KEY_C,1,e.KEY_C,0]],
        ['è',[e.KEY_LEFTSHIFT,1,e.KEY_EQUAL,1,e.KEY_EQUAL,0,e.KEY_LEFTSHIFT,0,e.KEY_E,1,e.KEY_E,0]],
        ['ß',[e.KEY_MINUS,1,e.KEY_MINUS,0]],
        ['$',[e.KEY_LEFTSHIFT,1,e.KEY_4,1,e.KEY_4,0,e.KEY_LEFTSHIFT,0]],
        ['f',[e.KEY_F,1,e.KEY_F,0]],
        ['m',[e.KEY_M,1,e.KEY_M,0]],
        ['j',[e.KEY_J,1,e.KEY_J,0]],
        ['w',[e.KEY_W,1,e.KEY_W,0]],
        ['l',[e.KEY_L,1,e.KEY_L,0]],
        ['b',[e.KEY_B,1,e.KEY_B,0]],
        ['v',[e.KEY_V,1,e.KEY_V,0]],
        # 50
        ['k',[e.KEY_K,1,e.KEY_K,0]],
        ['y',[e.KEY_Z,1,e.KEY_Z,0]],
        ['q',[e.KEY_Q,1,e.KEY_Q,0]],
        ['d',[e.KEY_D,1,e.KEY_D,0]],
        ['z',[e.KEY_Y,1,e.KEY_Y,0]],
        ['h',[e.KEY_H,1,e.KEY_H,0]],
        ['t',[e.KEY_T,1,e.KEY_T,0]],
        ['c',[e.KEY_C,1,e.KEY_C,0]],
        ['s',[e.KEY_S,1,e.KEY_S,0]],
        ['r',[e.KEY_R,1,e.KEY_R,0]],
        ['e',[e.KEY_E,1,e.KEY_E,0]],
        ['p',[e.KEY_P,1,e.KEY_P,0]],
        ['n',[e.KEY_N,1,e.KEY_N,0]],
        ['u',[e.KEY_U,1,e.KEY_U,0]],
        ['o',[e.KEY_O,1,e.KEY_O,0]],
        ['x',[e.KEY_X,1,e.KEY_X,0]],
        # 60
        ['g',[e.KEY_G,1,e.KEY_G,0]],
        ['a',[e.KEY_A,1,e.KEY_A,0]],
        ['-',[e.KEY_SLASH,1,e.KEY_SLASH,0]],
        ['.',[e.KEY_DOT,1,e.KEY_DOT,0]],
        [',',[e.KEY_COMMA,1,e.KEY_COMMA,0]],
        ['ä',[e.KEY_APOSTROPHE,1,e.KEY_APOSTROPHE,0]],
        ['ö',[e.KEY_SEMICOLON,1,e.KEY_SEMICOLON,0]],
        ['ü',[e.KEY_LEFTBRACE,1,e.KEY_LEFTBRACE,0]],
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        # 70
        None,
        ['Space',[e.KEY_SPACE,1,e.KEY_SPACE,0]],          # Space
        ['backstep',[e.KEY_INSERT,1,e.KEY_INSERT,0]],     # Insert
        None, 
        ['CODE backstep',[e.KEY_LEFTSHIFT,1,e.KEY_INSERT,1,e.KEY_INSERT,0,e.KEY_LEFTSHIFT,0]],  # shift-insert
        ['step down',[e.KEY_DOWN,1,e.KEY_DOWN,0]],        # cursor down
        ['step up',[e.KEY_UP,1,e.KEY_UP,0]],              # cursor up
        ['Return',[e.KEY_ENTER,1,e.KEY_ENTER,0]],         # Enter
        None,
        ['Tab',[e.KEY_TAB,1,e.KEY_TAB,0]],                 # tab
        ['T+',[e.KEY_PAGEUP,1,e.KEY_PAGEUP,0]],            # page-up
        ['T-',[e.KEY_PAGEDOWN,1,e.KEY_PAGEDOWN,0]],        # page-down
        ['CODE T-',[e.KEY_LEFTSHIFT,1,e.KEY_TAB,1,e.KEY_TAB,0,e.KEY_LEFTSHIFT,0]],        # shift-tab 
        ['CODE T+'],                                       # special: adjust step width for mouse
        ['Set Rand links',[e.KEY_ESC,1,e.KEY_ESC,0]],      # ESC
        ['Set Rand rechts',[e.KEY_LEFTCTRL,1,e.KEY_ESC,1,e.KEY_ESC,0,e.KEY_LEFTCTRL,0]],# CTRL-ESC (CODE+Rand links)
        # 80
        ['Rand lösen'],                                    # !!!!! still free
        ['CODE step down',[e.KEY_LEFT,1,e.KEY_LEFT,0]],    # cursor left
        ['CODE step up',[e.KEY_RIGHT,1,e.KEY_RIGHT,0]],    # cursor right
        ['form feed'],                                     # special form-feed (Papiereinzug)
        ['1 zeilig (stat)'],                               # 
        ['1,5 zeilig (stat)'],                             #
        ['2 zeilig (stat)'],                               #
        ['10 cpi (stat)'],                                 #
        ['12 cpi (stat)'],                                 #
        ['15 cpi (stat)'],                                 #
        None,
        None,
        None,
        None,
        None,
        None,
        # 90
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        ['CODE S',[e.KEY_LEFTCTRL,1,e.KEY_S,1,e.KEY_S,0,e.KEY_LEFTCTRL,0]], # CTRL-S
        None,
        # A0
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        # B0
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        ['CODE switch!'],                                  # escape sequence for CODE key
        None,
        None,
        None,
        None,
        # C0
        ['MODE 1',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F1,1,e.KEY_F1,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-ALT-F1
        ['MODE Q',[e.KEY_RIGHTALT,1,e.KEY_Q,1,e.KEY_Q,0,e.KEY_RIGHTALT,0]],                                   # @
        ['MODE A'],                                                                                   # special mouse left
        ['MODE Y'],                                                                                           # special mouse btn left 
        ['MODE 2',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F2,1,e.KEY_F2,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-ALT-F2
        ['MODE W'],                                                                                   # special mouse up
        ['MODE S'],                                                                                   # special mouse down
        ['MODE X'],                                                                                   # special mouse btn left hold
        ['MODE 3',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F3,1,e.KEY_F3,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-ALT-F3
        ['MODE E',[e.KEY_RIGHTALT,1,e.KEY_E,1,e.KEY_E,0,e.KEY_RIGHTALT,0]],                                   # €
        ['MODE D'],                                                                                   # special mouse right
        ['MODE C'],                                                                                   # special mouse btn right
        ['MODE 4',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F4,1,e.KEY_F4,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-ALT-F4
        ['MODE R',[e.KEY_F5,1,e.KEY_F5,0]],                                                                   # F5 (Refresh)
        ['MODE F',[e.KEY_F3,1,e.KEY_F3,0]],                                                                   # F3 (Find)
        ['MODE V'],                                                                                   # special mouse btn right hold
        # D0
        ['MODE 5',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F5,1,e.KEY_F5,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-ALT-F5
        ['MODE T',[e.KEY_LEFTSHIFT,1,e.KEY_PAGEUP,1,e.KEY_PAGEUP,0,e.KEY_LEFTSHIFT,0]],                       # shift-pageup (scrolling in lxterm)
        ['MODE G',[e.KEY_LEFTSHIFT,1,e.KEY_PAGEDOWN,1,e.KEY_PAGEDOWN,0,e.KEY_LEFTSHIFT,0]],                   # shift-pagedown (scrolldown in lxterm)
        ['MODE B'],                                                                                           # !!!!!!! free
        ['MODE 6',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F6,1,e.KEY_F6,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-ALT-F6
        ['MODE Z'],                                                                                           # !!!!!!! free
        ['MODE H',[e.KEY_LEFTSHIFT,1,e.KEY_LEFT,1,e.KEY_LEFT,0,e.KEY_LEFTSHIFT,0]],                           # shift-cursor-left (for marking)
        ['MODE N'],                                                                                           # !!!!!!! free
        ['MODE 7',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F7,1,e.KEY_F7,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-ALT-F7
        ['MODE U'],                                                                                           # !!!!!!! free
        ['MODE J',[e.KEY_LEFTSHIFT,1,e.KEY_DOWN,1,e.KEY_DOWN,0,e.KEY_LEFTSHIFT,0]],                           # shift-cursor-down (for marking)
        ['MODE M'],                                                                                           # !!!!!!! free
        ['MODE 8'],                                                                                           # !!!!!!! free
        ['MODE I'],                                                                                           # !!!!!!! free
        ['MODE K',[e.KEY_LEFTSHIFT,1,e.KEY_UP,1,e.KEY_UP,0,e.KEY_LEFTSHIFT,0]],                               # shift-cursor-up (for marking)
        ['MODE ,',[e.KEY_102ND,1,e.KEY_102ND,0]],                                                             # <
        # E0
        ['MODE 9'],                                                                                           # !!!!!!! free
        ['MODE O'],                                                                                           # !!!!!!! free
        ['MODE L',[e.KEY_LEFTSHIFT,1,e.KEY_RIGHT,1,e.KEY_RIGHT,0,e.KEY_LEFTSHIFT,0]],                         # shift-cursor-right (for marking)
        ['MODE .',[e.KEY_LEFTSHIFT,1,e.KEY_102ND,1,e.KEY_102ND,0,e.KEY_LEFTSHIFT,0]],                         # >
        ['MODE 0',[e.KEY_F11,1,e.KEY_F11,0]],                                                                 # F11 (fullscreen)
        ['MODE P',[e.KEY_RIGHTALT,1,e.KEY_7,1,e.KEY_7,0,e.KEY_RIGHTALT,0]],                                   # {
        ['MODE Ö',[e.KEY_RIGHTALT,1,e.KEY_8,1,e.KEY_8,0,e.KEY_RIGHTALT,0]],                                   # [
        ['MODE -',[e.KEY_LEFTCTRL,1,e.KEY_LEFTSHIFT,1,e.KEY_SLASH,1,e.KEY_SLASH,0,e.KEY_LEFTSHIFT,0,e.KEY_LEFTCTRL,0]], # CTRL-_
        ['MODE ß',[e.KEY_RIGHTALT,1,e.KEY_MINUS,1,e.KEY_MINUS,0,e.KEY_RIGHTALT,0]],                           # \
        ['MODE Ü',[e.KEY_RIGHTALT,1,e.KEY_0,1,e.KEY_0,0,e.KEY_RIGHTALT,0]],                                   # }
        ['MODE Ä',[e.KEY_RIGHTALT,1,e.KEY_9,1,e.KEY_9,0,e.KEY_RIGHTALT,0]],                                   # ]
        ['REL',[e.KEY_HOME,1,e.KEY_HOME,0]],                                                                  # Home
        ['MODE acutes',[e.KEY_RIGHTALT,1,e.KEY_RIGHTBRACE,1,e.KEY_RIGHTBRACE,0,e.KEY_RIGHTALT,0]],            # ~
        None,
        ['CODE REL',[e.KEY_END,1,e.KEY_END,0]],                                                               # End
        None,
        # F0
        None,
        None,
        None,
        None,
        ['MODE T+'],                                                                                # special switch typewriter/computer
        ['MODE T-',[e.KEY_LEFTALT,1,e.KEY_TAB,1,e.KEY_TAB,0,e.KEY_LEFTALT,0]],                                # ALT-Tab
        None,
        ['CODE backspace',[e.KEY_LEFTSHIFT,1,e.KEY_DELETE,1,e.KEY_DELETE,0,e.KEY_LEFTSHIFT,0]],               # shift-Delete
        ['2 zeilig (key)'],
        ['1 zeilig (key)'],
        ['10 CPI'],
        ['MODE backspace',[e.KEY_DELETE,1,e.KEY_DELETE,0]],                                                   # Delete
        ['backspace',[e.KEY_BACKSPACE,1,e.KEY_BACKSPACE,0]],                                                  # Backspace
        ['MODE form feed'],                                                                         # special shutdown -r now if next key is 'y'
        ['1,5 zeilig (key)'],
        ['12 CPI'],
        # 100
        None,
        ['CODE Q',[e.KEY_LEFTCTRL,1,e.KEY_Q,1,e.KEY_Q,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-Q
        ['CODE A',[e.KEY_LEFTCTRL,1,e.KEY_A,1,e.KEY_A,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-A
        ['CODE Y',[e.KEY_LEFTCTRL,1,e.KEY_Z,1,e.KEY_Z,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-Y
        None,
        ['CODE W',[e.KEY_LEFTCTRL,1,e.KEY_W,1,e.KEY_W,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-W
        None, # ['CODE S',[e.KEY_LEFTCTRL,1,e.KEY_S,1,e.KEY_S,0,e.KEY_LEFTCTRL,0]],
        ['CODE X',[e.KEY_LEFTCTRL,1,e.KEY_X,1,e.KEY_X,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-X
        None,
        ['CODE E',[e.KEY_LEFTCTRL,1,e.KEY_E,1,e.KEY_E,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-E
        ['CODE D',[e.KEY_LEFTCTRL,1,e.KEY_D,1,e.KEY_D,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-D
        ['CODE C',[e.KEY_LEFTCTRL,1,e.KEY_C,1,e.KEY_C,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-C
        None,
        ['CODE R',[e.KEY_LEFTCTRL,1,e.KEY_R,1,e.KEY_R,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-R
        ['CODE F',[e.KEY_LEFTCTRL,1,e.KEY_F,1,e.KEY_F,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-F
        ['CODE V',[e.KEY_LEFTCTRL,1,e.KEY_V,1,e.KEY_V,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-V
        # 110
        None,
        ['CODE T',[e.KEY_LEFTCTRL,1,e.KEY_T,1,e.KEY_T,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-T
        ['CODE G',[e.KEY_LEFTCTRL,1,e.KEY_G,1,e.KEY_G,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-G
        ['CODE B',[e.KEY_LEFTCTRL,1,e.KEY_B,1,e.KEY_B,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-B
        None,
        ['CODE Z',[e.KEY_LEFTCTRL,1,e.KEY_Y,1,e.KEY_Y,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-Y
        ['CODE H',[e.KEY_LEFTCTRL,1,e.KEY_H,1,e.KEY_H,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-H
        ['CODE N',[e.KEY_LEFTCTRL,1,e.KEY_N,1,e.KEY_N,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-N
        None,
        ['CODE U',[e.KEY_LEFTCTRL,1,e.KEY_U,1,e.KEY_U,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-U
        ['CODE J',[e.KEY_LEFTCTRL,1,e.KEY_J,1,e.KEY_J,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-J
        ['CODE M',[e.KEY_LEFTCTRL,1,e.KEY_M,1,e.KEY_M,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-M
        None,
        ['CODE I',[e.KEY_LEFTCTRL,1,e.KEY_I,1,e.KEY_I,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-I
        ['CODE K',[e.KEY_LEFTCTRL,1,e.KEY_K,1,e.KEY_K,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-K
        None,
        # 120
        None,
        ['CODE O',[e.KEY_LEFTCTRL,1,e.KEY_O,1,e.KEY_O,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-O
        ['CODE L',[e.KEY_LEFTCTRL,1,e.KEY_L,1,e.KEY_L,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-L
        None,
        None,
        ['CODE P',[e.KEY_LEFTCTRL,1,e.KEY_P,1,e.KEY_P,0,e.KEY_LEFTCTRL,0]],                                   # CTRL-P
        ['CODE Ö',[e.KEY_LEFTCTRL,1,e.KEY_RIGHTALT,1,e.KEY_8,1,e.KEY_8,0,e.KEY_RIGHTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-[
        None,
        None,
        ['CODE Ü',[e.KEY_LEFTCTRL,1,e.KEY_RIGHTALT,1,e.KEY_MINUS,1,e.KEY_MINUS,0,e.KEY_RIGHTALT,0,e.KEY_LEFTCTRL,0]], # CTRL-\
        ['CODE Ä',[e.KEY_LEFTCTRL,1,e.KEY_RIGHTALT,1,e.KEY_9,1,e.KEY_9,0,e.KEY_RIGHTALT,0,e.KEY_LEFTCTRL,0]]  # CTRL-]
    ]

    def key(self, kbd_data):
        keystat=['UP','DOWN']

        if kbd_data == 0xbb:
            data = self.serial.read()
            kbd_data=data[0]
            if self.verbose:
                print("+",hex(kbd_data),end='',sep='')
            kbd_data += 0x40
        if self.erika2uinput[kbd_data]:
            # Jetzt ist die richtige Taste gefunden
            if self.verbose:
                print(" =>",self.erika2uinput[kbd_data][0],flush=True)
            if len(self.erika2uinput[kbd_data])>1:
                # there are keycodes defined
                if self.echo:
                    return
                key_lst=self.erika2uinput[kbd_data][1]
                lenght=len(key_lst)
                i=0
                while i < lenght:
                    # iterate over keycodes
                    if self.verbose:
                        print(e.KEY[key_lst[i]],keystat[key_lst[i+1]],sep='.',end=', ')
                    self.ui.write(e.EV_KEY,key_lst[i],key_lst[i+1])
                    i += 2
                self.ui.syn()
                if self.verbose:
                    print(flush=True)
            else:
                # no keycodes defined, maybe a special key
                if self.verbose:
                    print("NO KEYS - start xkey",flush=True)
                self.xkey(kbd_data)
        else:
            # erika code not defined
            print("Error",kbd_data,"unknown!",flush=True)


    def xkey(self, kbd_data):
        """decode special keys"""
        if kbd_data == 0xf4:
            # Mode T+
            if self.echo:
                self.echo = False
                self.serial.write(b'\x91')
            else:
                self.echo = True
                self.serial.write(b'\x92')
            if self.verbose:
                print("Echo",self.echo)
            return
        if self.echo:
            return
        if kbd_data == 0x83:
            # Form Feed
            if self.verbose:
                print("Form Feed")
            self.serial.write(b'\x83')
        if kbd_data == 0xfd:
            # MODE+Form Feed - Reset if next is y
            if self.verbose:
                print("Reset? (press y)")
            if b'\x51' == self.serial.read():
                if self.verbose:
                    print('shutdown -r now')
                os.system('shutdown -r now')
        # Mouse movement
        elif kbd_data ==0x7d:
            # Code T+ - adjust step
            if self.step == 1:
                self.step=8
            elif self.step == 8:
                self.step=32
            else:
                self.step=1
            if self.verbose:
                print("Mouse step:",self.step)
        elif kbd_data == 0xc5:
            # Mode W - Mouse up
            if self.verbose:
                print("Mouse up",self.step)
            self.mui.write(e.EV_REL,e.REL_Y,-1*self.step)
        elif kbd_data == 0xc6:
            # Mode S - Mouse down
            if self.verbose:
                print("Mouse down",self.step)
            self.mui.write(e.EV_REL,e.REL_Y,self.step)
        elif kbd_data == 0xc2:
            # Mode A - Mouse left
            if self.verbose:
                print("Mouse left",self.step)
            self.mui.write(e.EV_REL,e.REL_X,-1*self.step)
        elif kbd_data == 0xca:
            # Mode D - Mouse right
            if self.verbose:
                print("Mouse right",self.step)
            self.mui.write(e.EV_REL,e.REL_X,self.step)
        elif kbd_data == 0xc3:
            # Mode Y - Mouse BTN left
            if self.verbose:
                print("Mouse BTN left")
            self.m_btn_left=False
            self.mui.write(e.EV_KEY,e.BTN_LEFT,1)
            self.mui.write(e.EV_KEY,e.BTN_LEFT,0)
        elif kbd_data == 0xc7:
            # Mode X - Mouse BTN left - Switch
            if self.m_btn_left:
                self.m_btn_left=False
                self.mui.write(e.EV_KEY,e.BTN_LEFT,0)
            else:
                self.m_btn_left=True
                self.mui.write(e.EV_KEY,e.BTN_LEFT,1)
            if self.verbose:
                print("Mouse BTN left", self.m_btn_left)
        elif kbd_data == 0xcB:
            # Mode C - Mouse BTN right
            if self.verbose:
                print("Mouse BTN right")
            self.mui.write(e.EV_KEY,e.BTN_RIGHT,1)
            self.mui.write(e.EV_KEY,e.BTN_RIGHT,0)
        elif kbd_data == 0xcF:
            # Mode V - Mouse BTN right - Switch
            if self.m_btn_right:
                self.m_btn_right=False
                self.mui.write(e.EV_KEY,e.BTN_RIGHT,0)
            else:
                self.m_btn_right=True
                self.mui.write(e.EV_KEY,e.BTN_RIGHT,1)
            if self.verbose:
                print("Mouse BTN right", self.m_btn_right)
        self.mui.syn()
