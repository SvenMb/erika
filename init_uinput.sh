#!/bin/sh

sudo gpasswd -a $USER input

sudo tee /etc/udev/rules.d/40-uinput.rules > /dev/null << 'EOF'
KERNEL=="uinput", MODE="0660", GROUP="input"
EOF

sudo udevadm control --reload-rules
sudo udevadm trigger

