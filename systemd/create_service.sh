#!/bin/sh

sudo cp default/erika /etc/default/
sudo cp system/erika.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl restart erika
