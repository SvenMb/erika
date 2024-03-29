# -*- coding: utf-8 -*-
#
#  erika.py
#  
#  Copyright 2022  <sven@muehlberg.net>
#  
from enum import Enum

class courier_de:
    def __init__(self,charset):
        self.co = None
        self.ch = b''
        if charset in ('cp858','if6000'):
            self.charset=charset
        else:
            print('unknown extra charset',charset,flush=True)
            charset = 'None'
        print ('extra charset:',self.charset,flush=True)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    utf82erika = {
        ### 7-bit ascii start ###
        # control chars
        "\b": b"\x72", # 0x08 backspace
        # "\t": b"\x79", # 0x09 tab
        "\t": b"",  # tab handled extern
        "\n": b"\x77", # 0x0a linefeed and carriage return
        "\r": b"\x78", # 0x0d carriage return
        "\f": b"", # form feed handled extern
        # Erika interprets
        # 0x77 as CR LF means NL
        # 0x78 only CR

        # 0x20
        # punctuation
        " ": b"\x71",
        "!": b"\x42",
        '"': b"\x43",
        "#": b"\x41",
        "$": b"\x48",
        "%": b"\x04",
        "&": b"\x02",
        "'": b"\x17",
        "(": b"\x1D",
        ")": b"\x1F",
        "*": b"\x1B",
        "+": b"\x25",
        ",": b"\x64",
        "-": b"\x62",
        ".": b"\x63",
        "/": b"\x40",

        # 0x30
        # digits
        "0": b"\x0D",
        "1": b"\x11",
        "2": b"\x10",
        "3": b"\x0F",
        "4": b"\x0E",
        "5": b"\x0C",
        "6": b"\x0B",
        "7": b"\x0A",
        "8": b"\x09",
        "9": b"\x08",

        # more punctuation
        ":": b"\x13",
        ";": b"\x3B",
        ">": b"\xa6\x0e\x29\xa6\xfa\x2b\xa6\xf9\xee\x71",
        "=": b"\x2E",
        "<": b"\xa6\x0e\x2b\xa6\xfa\x29\xa6\xf9\xee\x71",
        "?": b"\x35",

        # 0x40
        "@": b"\xa6\xfd\xa9\x61\xa5\xfe\xa6\x06\xa9\x20\xa5\x02\xa6\xfe\xee\x71",
        # upper case letters
        "A": b"\x30",
        "B": b"\x18",
        "C": b"\x20",
        "D": b"\x14",
        "E": b"\x34",
        "F": b"\x3E",
        "G": b"\x1C",
        "H": b"\x12",
        "I": b"\x21",
        "J": b"\x32",
        "K": b"\x24",
        "L": b"\x2C",
        "M": b"\x16",
        "N": b"\x2A",
        "O": b"\x1E",
        # 0x50
        "P": b"\x2F",
        "Q": b"\x1A",
        "R": b"\x36",
        "S": b"\x33",
        "T": b"\x37",
        "U": b"\x28",
        "V": b"\x22",
        "W": b"\x2D",
        "X": b"\x26",
        "Y": b"\x31",
        "Z": b"\x38",
        "[": b"\xa6\xf9\x29\xa6\x2b\x2b\xa6\xde\xa5\xfd\xa9\x27\xa5\x03\xee\x71",
        "\\": b"\xa6\x01\xa9\x17\xa6\x09\xa5\x03\xa9\x17\xa6\x09\xa5\x03\xa9\x17\xa5\xfa\xa6\xf0\xee\x71",
        "]": b"\xa6\xf9\x2b\xa6\x2b\x29\xa6\xde\xa5\x03\xa9\x27\xa5\xfd\xee\x71",

        # punctuation
        "^": b"\x19\x71",
        "_": b"\x01",
        # 0x60
        "`": b"\x2B\x71",

        # lower case letters
        "a": b"\x61",
        "b": b"\x4E",
        "c": b"\x57",
        "d": b"\x53",
        "e": b"\x5A",
        "f": b"\x49",
        "g": b"\x60",
        "h": b"\x55",
        "i": b"\x05",
        "j": b"\x4B",
        "k": b"\x50",
        "l": b"\x4D",
        "m": b"\x4A",
        "n": b"\x5C",
        "o": b"\x5E",
        # 0x70
        "p": b"\x5B",
        "q": b"\x52",
        "r": b"\x59",
        "s": b"\x58",
        "t": b"\x56",
        "u": b"\x5D",
        "v": b"\x4F",
        "w": b"\x4C",
        "x": b"\x5F",
        "y": b"\x51",
        "z": b"\x54",

        # special chars
        "{": b"\xa9\x1d\xa6\x06\x39\xa6\xfb\xee",
        "|": b"\x27",
        "}": b"\xa9\x1f\xa6\x06\x39\xa6\xfb\xee",
        "~": b"\xa6\xf4\xa9\x64\xa6\x16\xa5\x03\x2b\xa5\x03\xa6\xeb\xa9\x64\xa6\x0c\xa5\xfa\xee\x71",    # 0x7e
        # 0x7f backspace

        ### 7-bit ascii end ###  

        ### utf-8 start ###
        "£": b"\x06",       # 0xC2 0xa3
        "§": b"\x3D",       # 0xC2 0xA7
        "¨": b"\x03\x71",   # 0xC2 0xA8
        "°": b"\x39",       # 0xC2 0xB0
        "²": b"\x15",       # 0xC2 0xB2
        "³": b"\x23",       # 0xC2 0xB3

        # umlauts, accents
        "Ä": b"\x3F",       # 0xC3 0x84
        "Ö": b"\x3C",       # 0xC3 0x96
        "Ü": b"\x3A",       # 0xC3 0x9C
        "ß": b"\x47",       # 0xC3 0x9F
        "ä": b"\x65",       # 0xC3 0xA4
        "ç": b"\x45",       # 0xC3 0xA7
        "è": b"\x46",       # 0xC3 0xA8
        "é": b"\x44",       # 0xC3 0xA9
        b'\xc2\xb5'.decode(): b"\x07",       # 0xC2 0xB5 µ
        "ö": b"\x66",       # 0xC3 0xB6
        "ü": b"\x67",       # 0xC3 0xBC
        "`": b"\x29\x71",   # 0xE2 0x80 0xB2
        "€": b"\xa9\x20\x2E", # 0xE2 0x82 0xAC

        ### utf-8 end ###
    }

    cp8582utf8 = {

        ### cp858 (cp850 with €) start ###

        0x7f: b'\b',                 # Backspace
        0x81: "ü".encode('utf-8'),   # 0x81 ü
        0x82: "é".encode('utf-8'),   # 0x82 é
        0x84: "ä".encode('utf-8'),   # 0x84 ä
        0x87: "ç".encode('utf-8'),   # 0x87 ç
        0x8a: "è".encode('utf-8'),   # 0x8a è
        0x8e: "Ä".encode('utf-8'),   # 0x8e Ä
        0x94: "ö".encode('utf-8'),   # 0x94 ö
        0x99: "Ö".encode('utf-8'),   # 0x99 Ö
        0x9a: "Ü".encode('utf-8'),   # 0x9a Ü
        0x9c: "£".encode('utf-8'),   # 0x9c £
        0xd5: "€".encode('utf-8'),
        0xe1: "ß".encode('utf-8'),   # 0xe1 ß
        0xe6: "µ".encode('utf-8'),   # 0xe6 µ
        0xf5: "§".encode('utf-8'),   # 0xf5 §
        0xf8: "°".encode('utf-8'),   # 0xf8 °
        0xfc: "³".encode('utf-8'),   # 0xfc ³
        0xfd: "²".encode('utf-8'),   # 0xfd ²

        ### cp858 end ###
    }

    if6000 = {
        ### if6000 start ###

        0x7f: b'\b',
        0x40: "§".encode('utf-8'),
        0x5b: "Ä".encode('utf-8'),
        0x5c: "Ö".encode('utf-8'),
        0x5d: "Ü".encode('utf-8'),
        0x7b: "ä".encode('utf-8'),
        0x7c: "ö".encode('utf-8'),
        0x7d: "ü".encode('utf-8'),
        0x7e: "ß".encode('utf-8'),
        0x82: "é".encode('utf-8'),
        0x87: "ç".encode('utf-8'),
        0x8a: "è".encode('utf-8'),
        0x9c: "£".encode('utf-8'),
        0xb0: "³".encode('utf-8'),
        0xb3: "|".encode('utf-8'),
        0xe6: "µ".encode('utf-8'),
        0xf3: "`".encode('utf-8'),
        0xf8: "°".encode('utf-8'),
        0xfd: "²".encode('utf-8'),
        ### if6000 end ###
    }


    def decode(self, char):
        # read multibyte chars
        if self.co and self.co > 1:
            self.co -= 1
            self.ch += char
            return b''
        elif self.co and self.co == 1:
            self.co = None
            char = self.ch + char
            self.ch= b''
        elif char[0] in (0xc2, 0xc3):
            self.co = 1
            self.ch += char
            return b''
        elif char[0] == 0xe2:
            self.co = 2
            self.ch += char
            return b''

        # replace cp858 chars with utf-8 ones
        elif self.charset == 'cp858' and char[0] in self.cp8582utf8.keys():
            char = self.cp8582utf8[char[0]]

        # replace if6000 chars with utf-8 ones
        elif self.charset == 'if6000' and char[0] in self.if6000.keys():
            char = self.if6000[char[0]]

        # find known utf-8 chars and return bytes for erika
        try:
            if char.decode() in self.utf82erika.keys():
                return(self.utf82erika[char.decode()])
        except:
            print('char not possible:', char) 
            return(self.utf82erika[" "])
        # if not found, then return space and error for log
        print('char not defined:', char) 
        return(self.utf82erika[" "])

