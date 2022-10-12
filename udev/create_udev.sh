#!/bin/sh

set -x

sudo cp 98-erika.rules /etc/udev/rules.d/
sudo udevadm control --reload
