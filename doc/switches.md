# keycodes and states for switches

## keycodes send by erika 3004/3005/3006/3015/3016

Even if the switches on the left side of the keyboard have different meaning on 3005 and 3006 they send same key codes.
Only 3004 send different codes.

I have tested all the erika models  and got that table:

switch                   | 3004 | 3005 | 3006 | 3015 | 3016
-------------------------|------|------|------|------|------
upper switch, upper pos  | 0x86 | 0xf8 | 0xf8 | 0xf8 | 0xf8
upper switch, middle pos | 0x85 | 0xfe | 0xfe | 0xfe | 0xfe
upper switch, lower pos  | 0x84 | 0xf9 | 0xf9 | 0xf9 | 0xf9
lower switch, upper pos  | 0x88 | 0xff | 0xff | 0xff | 0xff
lower switch, lower pos  | 0x87 | 0xfa | 0xfa | 0xfa | 0xfa

so from 3005 and up there is a special code for the switches, while 3004 send it as state of typewriter.

## when sending the disconnect code (0x92)

*this code disconnects the typewriter from the keyboard, for computer use and send information about the state of the typewriter*

### erika 3004

* sends only state of typewriter and switches together
  * state of cpi, one of:
    * 0x87 - 10cpi
    * 0x88 - 12cpi
  * state of line spacing, one of
    * 0x84 - 1 line
    * 0x85 - 1,5 line
    * 0x86 - 1,5 line

*be aware erika 3004 may send 0x85 (0x85) first and then the correct line spacing.*

### erika 3005, 3006, 3015, 3016

* sends state of typewriter
  * state of cpi, one of:
    * 0x87 - 10cpi
    * 0x88 - 12cpi
    * 0x89 - 15cpi
  * state of line spacing, one of
    * 0x84 - 1 line
    * 0x85 - 1,5 line
    * 0x86 - 1,5 line

* sends state of switches
  * one byte for each switch (2), see above table

### Conclusion

based on this it is possible to auto switch between 3004 and 3005 (and above with mode key)
