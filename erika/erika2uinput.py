from evdev import ecodes as e

"""
possible ecodes:
 Event type 1 (EV_KEY)
    Event code 1 (KEY_ESC)
    Event code 2 (KEY_1)
    Event code 3 (KEY_2)
    Event code 4 (KEY_3)
    Event code 5 (KEY_4)
    Event code 6 (KEY_5)
    Event code 7 (KEY_6)
    Event code 8 (KEY_7)
    Event code 9 (KEY_8)
    Event code 10 (KEY_9)
    Event code 11 (KEY_0)
    Event code 12 (KEY_MINUS)
    Event code 13 (KEY_EQUAL)
    Event code 14 (KEY_BACKSPACE)
    Event code 15 (KEY_TAB)
    Event code 16 (KEY_Q)
    Event code 17 (KEY_W)
    Event code 18 (KEY_E)
    Event code 19 (KEY_R)
    Event code 20 (KEY_T)
    Event code 21 (KEY_Y)
    Event code 22 (KEY_U)
    Event code 23 (KEY_I)
    Event code 24 (KEY_O)
    Event code 25 (KEY_P)
    Event code 26 (KEY_LEFTBRACE)
    Event code 27 (KEY_RIGHTBRACE)
    Event code 28 (KEY_ENTER)
    Event code 29 (KEY_LEFTCTRL)
    Event code 30 (KEY_A)
    Event code 31 (KEY_S)
    Event code 32 (KEY_D)
    Event code 33 (KEY_F)
    Event code 34 (KEY_G)
    Event code 35 (KEY_H)
    Event code 36 (KEY_J)
    Event code 37 (KEY_K)
    Event code 38 (KEY_L)
    Event code 39 (KEY_SEMICOLON)
    Event code 40 (KEY_APOSTROPHE)
    Event code 41 (KEY_GRAVE)
    Event code 42 (KEY_LEFTSHIFT)
    Event code 43 (KEY_BACKSLASH)
    Event code 44 (KEY_Z)
    Event code 45 (KEY_X)
    Event code 46 (KEY_C)
    Event code 47 (KEY_V)
    Event code 48 (KEY_B)
    Event code 49 (KEY_N)
    Event code 50 (KEY_M)
    Event code 51 (KEY_COMMA)
    Event code 52 (KEY_DOT)
    Event code 53 (KEY_SLASH)
    Event code 54 (KEY_RIGHTSHIFT)
    Event code 55 (KEY_KPASTERISK)
    Event code 56 (KEY_LEFTALT)
    Event code 57 (KEY_SPACE)
    Event code 58 (KEY_CAPSLOCK)
    Event code 59 (KEY_F1)
    Event code 60 (KEY_F2)
    Event code 61 (KEY_F3)
    Event code 62 (KEY_F4)
    Event code 63 (KEY_F5)
    Event code 64 (KEY_F6)
    Event code 65 (KEY_F7)
    Event code 66 (KEY_F8)
    Event code 67 (KEY_F9)
    Event code 68 (KEY_F10)
    Event code 69 (KEY_NUMLOCK)
    Event code 70 (KEY_SCROLLLOCK)
    Event code 71 (KEY_KP7)
    Event code 72 (KEY_KP8)
    Event code 73 (KEY_KP9)
    Event code 74 (KEY_KPMINUS)
    Event code 75 (KEY_KP4)
    Event code 76 (KEY_KP5)
    Event code 77 (KEY_KP6)
    Event code 78 (KEY_KPPLUS)
    Event code 79 (KEY_KP1)
    Event code 80 (KEY_KP2)
    Event code 81 (KEY_KP3)
    Event code 82 (KEY_KP0)
    Event code 83 (KEY_KPDOT)
    Event code 85 (KEY_ZENKAKUHANKAKU)
    Event code 86 (KEY_102ND)
    Event code 87 (KEY_F11)
    Event code 88 (KEY_F12)
    Event code 89 (KEY_RO)
    Event code 90 (KEY_KATAKANA)
    Event code 91 (KEY_HIRAGANA)
    Event code 92 (KEY_HENKAN)
    Event code 93 (KEY_KATAKANAHIRAGANA)
    Event code 94 (KEY_MUHENKAN)
    Event code 95 (KEY_KPJPCOMMA)
    Event code 96 (KEY_KPENTER)
    Event code 97 (KEY_RIGHTCTRL)
    Event code 98 (KEY_KPSLASH)
    Event code 99 (KEY_SYSRQ)
    Event code 100 (KEY_RIGHTALT)
    Event code 102 (KEY_HOME)
    Event code 103 (KEY_UP)
    Event code 104 (KEY_PAGEUP)
    Event code 105 (KEY_LEFT)
    Event code 106 (KEY_RIGHT)
    Event code 107 (KEY_END)
    Event code 108 (KEY_DOWN)
    Event code 109 (KEY_PAGEDOWN)
    Event code 110 (KEY_INSERT)
    Event code 111 (KEY_DELETE)
    Event code 113 (KEY_MUTE)
    Event code 114 (KEY_VOLUMEDOWN)
    Event code 115 (KEY_VOLUMEUP)
    Event code 116 (KEY_POWER)
    Event code 117 (KEY_KPEQUAL)
    Event code 119 (KEY_PAUSE)
    Event code 121 (KEY_KPCOMMA)
    Event code 122 (KEY_HANGUEL)
    Event code 123 (KEY_HANJA)
    Event code 124 (KEY_YEN)
    Event code 125 (KEY_LEFTMETA)
    Event code 126 (KEY_RIGHTMETA)
    Event code 127 (KEY_COMPOSE)
    Event code 128 (KEY_STOP)
    Event code 129 (KEY_AGAIN)
    Event code 130 (KEY_PROPS)
    Event code 131 (KEY_UNDO)
    Event code 132 (KEY_FRONT)
    Event code 133 (KEY_COPY)
    Event code 134 (KEY_OPEN)
    Event code 135 (KEY_PASTE)
    Event code 136 (KEY_FIND)
    Event code 137 (KEY_CUT)
    Event code 138 (KEY_HELP)
    Event code 140 (KEY_CALC)
    Event code 142 (KEY_SLEEP)
    Event code 150 (KEY_WWW)
    Event code 152 (KEY_SCREENLOCK)
    Event code 158 (KEY_BACK)
    Event code 159 (KEY_FORWARD)
    Event code 161 (KEY_EJECTCD)
    Event code 163 (KEY_NEXTSONG)
    Event code 164 (KEY_PLAYPAUSE)
    Event code 165 (KEY_PREVIOUSSONG)
    Event code 166 (KEY_STOPCD)
    Event code 173 (KEY_REFRESH)
    Event code 176 (KEY_EDIT)
    Event code 177 (KEY_SCROLLUP)
    Event code 178 (KEY_SCROLLDOWN)
    Event code 179 (KEY_KPLEFTPAREN)
    Event code 180 (KEY_KPRIGHTPAREN)
    Event code 183 (KEY_F13)
    Event code 184 (KEY_F14)
    Event code 185 (KEY_F15)
    Event code 186 (KEY_F16)
    Event code 187 (KEY_F17)
    Event code 188 (KEY_F18)
    Event code 189 (KEY_F19)
    Event code 190 (KEY_F20)
    Event code 191 (KEY_F21)
    Event code 192 (KEY_F22)
    Event code 193 (KEY_F23)
    Event code 194 (KEY_F24)
    Event code 240 (KEY_UNKNOWN)
 """

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
    ['Space',[e.KEY_SPACE,1,e.KEY_SPACE,0]],                 # 1 Zeichen rechts
    ['backstep',[e.KEY_INSERT,1,e.KEY_INSERT,0]],       # 1 Zeichen links
    None,               # 1/2 Zeichen rechts 
    ['CODE backstep',[e.KEY_LEFTSHIFT,1,e.KEY_INSERT,1,e.KEY_INSERT,0,e.KEY_LEFTSHIFT,0]],  # 1/2 Zeichen links
    ['step down',[e.KEY_DOWN,1,e.KEY_DOWN,0]],      # 1/2 Zeile nach unten
    ['step up',[e.KEY_UP,1,e.KEY_UP,0]],        # 1/2 Zeile nach oben
    ['Return',[e.KEY_ENTER,1,e.KEY_ENTER,0]],         # CR+LF
    None,               # CR
    ['Tab',[e.KEY_TAB,1,e.KEY_TAB,0]],            # next Tab
    ['T+',[e.KEY_PAGEUP,1,e.KEY_PAGEUP,0]],             # Tab setzen
    ['T-',[e.KEY_PAGEDOWN,1,e.KEY_PAGEDOWN,0]],             # Tab löschen
    ['CODE T-',[e.KEY_LEFTSHIFT,1,e.KEY_TAB,1,e.KEY_TAB,0,e.KEY_LEFTSHIFT,0]],        # alle Tab löschen 
    ['CODE T+'],        # Standardtabs setzen
    ['Set Rand links',[e.KEY_ESC,1,e.KEY_ESC,0]], # Rand links setzen
    ['Set Rand rechts',[e.KEY_LEFTCTRL,1,e.KEY_ESC,1,e.KEY_ESC,0,e.KEY_LEFTCTRL,0]],# Rand rechts setzen
    # 80
    ['Rand lösen'],     # Rand lösen
    ['CODE step down',[e.KEY_LEFT,1,e.KEY_LEFT,0]], # 1/20 Zeile nach unten
    ['CODE step up',[e.KEY_RIGHT,1,e.KEY_RIGHT,0]],   # 1/20 Zeile nach oben
    ['form feed'],      # Papiereinzug
    ['1 zeilig (stat)'],# Zeilenabstand 1
    ['1,5 zeilig (stat)'],# Zeilenabstand 1,5
    ['2 zeilig (stat)'],# Zeilenabstand 2
    ['10 cpi (stat)'],  # 10 cpi
    ['12 cpi (stat)'],  # 12 cpi
    ['15 cpi (stat)'],  # 15 cpi
    None,
    None,               # set delete off 
    None,               # set delete on
    None,               # Rückwärtsdruck aus
    None,               # Rückwärtsdruck an
    None,               # Randlösen dauerhaft an
    # 90
    None,               # Randlösen dauerhaft aus 
    None,               # echo off
    None,               # echo on
    None,               # reset
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
    ['CODE S',[e.KEY_LEFTCTRL,1,e.KEY_S,1,e.KEY_S,0,e.KEY_LEFTCTRL,0]],
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
    ['CODE switch!'],
    None,
    None,
    None,
    None,
    # C0
    ['MODE 1',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F1,1,e.KEY_F1,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE Q',[e.KEY_RIGHTALT,1,e.KEY_Q,1,e.KEY_Q,0,e.KEY_RIGHTALT,0]], # @
    ['MODE A'],
    ['MODE Y'],
    ['MODE 2',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F2,1,e.KEY_F2,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE W'],
    ['MODE S'],
    ['MODE X'],
    ['MODE 3',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F3,1,e.KEY_F3,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE E',[e.KEY_RIGHTALT,1,e.KEY_E,1,e.KEY_E,0,e.KEY_RIGHTALT,0]], # €
    ['MODE D'], 
    ['MODE C'],
    ['MODE 4',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F4,1,e.KEY_F4,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE R',[e.KEY_F5,1,e.KEY_F5,0]],
    ['MODE F',[e.KEY_F3,1,e.KEY_F3,0]],
    ['MODE V'],
    # D0
    ['MODE 5',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F5,1,e.KEY_F5,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE T',[e.KEY_LEFTCTRL,1,e.KEY_PAGEUP,1,e.KEY_PAGEUP,0,e.KEY_LEFTSHIFT,0]],
    ['MODE G',[e.KEY_LEFTCTRL,1,e.KEY_PAGEUP,1,e.KEY_PAGEUP,0,e.KEY_LEFTSHIFT,0]],
    ['MODE B'],
    ['MODE 6',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F6,1,e.KEY_F6,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE Z'],
    ['MODE H',[e.KEY_LEFTSHIFT,1,e.KEY_LEFT,1,e.KEY_LEFT,0,e.KEY_LEFTSHIFT,0]],
    ['MODE N'],
    ['MODE 7',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F7,1,e.KEY_F7,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE U'],
    ['MODE J',[e.KEY_LEFTSHIFT,1,e.KEY_DOWN,1,e.KEY_DOWN,0,e.KEY_LEFTSHIFT,0]],
    ['MODE M'],
    ['MODE 8',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F8,1,e.KEY_F8,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE I'],
    ['MODE K',[e.KEY_LEFTSHIFT,1,e.KEY_UP,1,e.KEY_UP,0,e.KEY_LEFTSHIFT,0]],
    ['MODE ,',[e.KEY_102ND,1,e.KEY_102ND,0]],
    # E0
    ['MODE 9',[e.KEY_LEFTCTRL,1,e.KEY_LEFTALT,1,e.KEY_F9,1,e.KEY_F9,0,e.KEY_LEFTALT,0,e.KEY_LEFTCTRL,0]],
    ['MODE O'],
    ['MODE L',[e.KEY_LEFTSHIFT,1,e.KEY_RIGHT,1,e.KEY_RIGHT,0,e.KEY_LEFTSHIFT,0]],
    ['MODE .',[e.KEY_LEFTSHIFT,1,e.KEY_102ND,1,e.KEY_102ND,0,e.KEY_LEFTSHIFT,0]],
    ['MODE 0',[e.KEY_F11,1,e.KEY_F11,0]],
    ['MODE P',[e.KEY_RIGHTALT,1,e.KEY_7,1,e.KEY_7,0,e.KEY_RIGHTALT,0]],
    ['MODE Ö',[e.KEY_RIGHTALT,1,e.KEY_8,1,e.KEY_8,0,e.KEY_RIGHTALT,0]],
    ['MODE -',[e.KEY_LEFTCTRL,1,e.KEY_LEFTSHIFT,1,e.KEY_SLASH,1,e.KEY_SLASH,0,e.KEY_LEFTSHIFT,0,e.KEY_LEFTCTRL,0]],
    ['MODE ß',[e.KEY_RIGHTALT,1,e.KEY_MINUS,1,e.KEY_MINUS,0,e.KEY_RIGHTALT,0]],
    ['MODE Ü',[e.KEY_RIGHTALT,1,e.KEY_0,1,e.KEY_0,0,e.KEY_RIGHTALT,0]],
    ['MODE Ä',[e.KEY_RIGHTALT,1,e.KEY_9,1,e.KEY_9,0,e.KEY_RIGHTALT,0]],
    ['REL',[e.KEY_HOME,1,e.KEY_HOME,0]],
    ['MODE acutes',[e.KEY_RIGHTALT,1,e.KEY_RIGHTBRACE,1,e.KEY_RIGHTBRACE,0,e.KEY_RIGHTALT,0]],
    None,
    ['CODE REL',[e.KEY_END,1,e.KEY_END,0]],
    None,
    # F0
    None,
    None,
    None,
    None,
    ['MODE T+'],
    ['MODE T-',[e.KEY_LEFTALT,1,e.KEY_TAB,1,e.KEY_TAB,0,e.KEY_LEFTALT,0]],
    None,
    ['CODE backspace',[e.KEY_LEFTSHIFT,1,e.KEY_DELETE,1,e.KEY_DELETE,0,e.KEY_LEFTSHIFT,0]],
    ['2 zeilig (key)'],
    ['1 zeilig (key)'],
    ['10 CPI'],
    ['MODE backspace',[e.KEY_DELETE,1,e.KEY_DELETE,0]],
    ['backspace',[e.KEY_BACKSPACE,1,e.KEY_BACKSPACE,0]],
    ['MODE form feed'],
    ['1,5 zeilig (key)'],
    ['12 CPI'],
    # 100
    None,
    ['CODE Q',[e.KEY_LEFTCTRL,1,e.KEY_Q,1,e.KEY_Q,0,e.KEY_LEFTCTRL,0]],
    ['CODE A',[e.KEY_LEFTCTRL,1,e.KEY_A,1,e.KEY_A,0,e.KEY_LEFTCTRL,0]],
    ['CODE Y',[e.KEY_LEFTCTRL,1,e.KEY_Z,1,e.KEY_Z,0,e.KEY_LEFTCTRL,0]],
    None,
    ['CODE W',[e.KEY_LEFTCTRL,1,e.KEY_W,1,e.KEY_W,0,e.KEY_LEFTCTRL,0]],
    None, # ['CODE S',[e.KEY_LEFTCTRL,1,e.KEY_S,1,e.KEY_S,0,e.KEY_LEFTCTRL,0]],
    ['CODE X',[e.KEY_LEFTCTRL,1,e.KEY_X,1,e.KEY_X,0,e.KEY_LEFTCTRL,0]],
    None,
    ['CODE E',[e.KEY_LEFTCTRL,1,e.KEY_E,1,e.KEY_E,0,e.KEY_LEFTCTRL,0]],
    ['CODE D',[e.KEY_LEFTCTRL,1,e.KEY_D,1,e.KEY_D,0,e.KEY_LEFTCTRL,0]],
    ['CODE C',[e.KEY_LEFTCTRL,1,e.KEY_C,1,e.KEY_C,0,e.KEY_LEFTCTRL,0]],
    None,
    ['CODE R',[e.KEY_LEFTCTRL,1,e.KEY_R,1,e.KEY_R,0,e.KEY_LEFTCTRL,0]],
    ['CODE F',[e.KEY_LEFTCTRL,1,e.KEY_F,1,e.KEY_F,0,e.KEY_LEFTCTRL,0]],
    ['CODE V',[e.KEY_LEFTCTRL,1,e.KEY_V,1,e.KEY_V,0,e.KEY_LEFTCTRL,0]],
    # 110
    None,
    ['CODE T',[e.KEY_LEFTCTRL,1,e.KEY_T,1,e.KEY_T,0,e.KEY_LEFTCTRL,0]],
    ['CODE G',[e.KEY_LEFTCTRL,1,e.KEY_G,1,e.KEY_G,0,e.KEY_LEFTCTRL,0]],
    ['CODE B',[e.KEY_LEFTCTRL,1,e.KEY_B,1,e.KEY_B,0,e.KEY_LEFTCTRL,0]],
    None,
    ['CODE Z',[e.KEY_LEFTCTRL,1,e.KEY_Y,1,e.KEY_Y,0,e.KEY_LEFTCTRL,0]],
    ['CODE H',[e.KEY_LEFTCTRL,1,e.KEY_H,1,e.KEY_H,0,e.KEY_LEFTCTRL,0]],
    ['CODE N',[e.KEY_LEFTCTRL,1,e.KEY_N,1,e.KEY_N,0,e.KEY_LEFTCTRL,0]],
    None,
    ['CODE U',[e.KEY_LEFTCTRL,1,e.KEY_U,1,e.KEY_U,0,e.KEY_LEFTCTRL,0]],
    ['CODE J',[e.KEY_LEFTCTRL,1,e.KEY_J,1,e.KEY_J,0,e.KEY_LEFTCTRL,0]],
    ['CODE M',[e.KEY_LEFTCTRL,1,e.KEY_M,1,e.KEY_M,0,e.KEY_LEFTCTRL,0]],
    None,
    ['CODE I',[e.KEY_LEFTCTRL,1,e.KEY_I,1,e.KEY_I,0,e.KEY_LEFTCTRL,0]],
    ['CODE K',[e.KEY_LEFTCTRL,1,e.KEY_K,1,e.KEY_K,0,e.KEY_LEFTCTRL,0]],
    None,
    # 120
    None,
    ['CODE O',[e.KEY_LEFTCTRL,1,e.KEY_O,1,e.KEY_O,0,e.KEY_LEFTCTRL,0]],
    ['CODE L',[e.KEY_LEFTCTRL,1,e.KEY_L,1,e.KEY_L,0,e.KEY_LEFTCTRL,0]],
    None,
    None,
    ['CODE P',[e.KEY_LEFTCTRL,1,e.KEY_P,1,e.KEY_P,0,e.KEY_LEFTCTRL,0]],
    ['CODE Ö',[e.KEY_LEFTCTRL,1,e.KEY_RIGHTALT,1,e.KEY_8,1,e.KEY_8,0,e.KEY_RIGHTALT,0,e.KEY_LEFTCTRL,0]],
    None,
    None,
    ['CODE Ü',[e.KEY_LEFTCTRL,1,e.KEY_RIGHTALT,1,e.KEY_MINUS,1,e.KEY_MINUS,0,e.KEY_RIGHTALT,0,e.KEY_LEFTCTRL,0]],
    ['CODE Ä',[e.KEY_LEFTCTRL,1,e.KEY_RIGHTALT,1,e.KEY_9,1,e.KEY_9,0,e.KEY_RIGHTALT,0,e.KEY_LEFTCTRL,0]]
]