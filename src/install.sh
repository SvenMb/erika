#!/bin/sh

sudo mkdir /var/lib/erika
sudo cp -R erika /var/lib/erika/
sudo cp -R setperm.sh /var/lib/erika/
sudo cp erika.py erika_set.py /var/lib/erika/
sudo ln -s /var/lib/erika/erika_set.py /usr/bin/
sudo systemctl daemon-reload
sudo systemctl restart erika
