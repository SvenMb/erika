## Use your erika typewriter as keyboard and printer (and mouse)

![System overview](doc/erika_raspberry.jpg)

### Compatible systems

You need a system with uinput (like linux), python3 and a TTL-serial port with CTS (can be done via usb-serial adapter).

I use a raspberry, because of this everything will be tested and prepared to use it this way. 

### Install

see [here](doc/install.md)

### Use together with RunCPM

with a very small patch you can use the erika as "lst:" in RunCPM. Printing will be done without delay, every char will be printed directly.

Patch file: [RunCPM.patch](doc/RunCPM.patch)

orig Repository: [https://github.com/MockbaTheBorg/RunCPM.git](https://github.com/MockbaTheBorg/RunCPM.git)



