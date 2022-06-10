#!/bin/sh
# echo "Hallo von setperm! device=$1"
[ -z $1 ] && exit 
chgrp lp $1
chmod 660 $1
if ! [ -d /dev/erika ]; then
  mkdir -m 750 /dev/erika
  chgrp lp /dev/erika
fi
ln -fs $1 /dev/erika/erika

