#!/bin/sh

LC_ALL=C ppdc erika.drv
# lpadmin -p Test -P ppd/erika.ppd -v serial:/dev/ttyAMA0
# lpadmin -p Test -P ppd/erika.ppd -v serial:/dev/erika/erika
