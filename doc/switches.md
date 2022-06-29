## keycodes send by erika 3004/3005/3006/3015/3016

Even if the switches on the left side of the keyboard have different meaning on 3005 and 3006 they send same key codes.

I have tested all the erika models  and got that table:

switch                   | 3004 | 3005 | 3006 | 3015 | 3016
-------------------------|------|------|------|------|------
upper switch, upper pos  |      | 0xf8 | 0xf8 | 0xf8 | 0xf8
upper switch, middle pos |      | 0xfe | 0xfe | 0xfe | 0xfe
upper switch, lower pos  |      | 0xf9 | 0xf9 | 0xf9 | 0xf9
lower switch, upper pos  |      | 0xff | 0xff | 0xff | 0xff
lower switch, lower pos  |      | 0xfa | 0xfa | 0xfa | 0xfa
