#!/bin/sh

user=$(whoami)
sudo socat -d -d PTY,raw,echo=0,link=/dev/ttyS10,user=$user PTY,raw,echo=0,link=/dev/ttyS11,user=$user
