#!/bin/sh

sudo cp filter/erika /usr/lib/cups/filter/
LC_ALL=C ppdc erika.drv
lpadmin -p Erika -P ppd/erika.ppd -v serial:/dev/erika/erika
