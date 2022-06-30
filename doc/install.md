### Install service

#### do all 

#### manual install

1. change to project directory
2.  install python-evdev  
...```console
user@host:~/dev/erika$ sudo pip3 install evdev
...```
3.  copy src to /var/lib/erika
```console
sudo cp -R src /var/lib/erika
```
4. copy service/erika.service to /etc/systemd/system/erika.service
...```console
user@host:~/dev/erika$ sudo cp service/erika.service /etc/systemd/system/erika.service
...```
5. copy default/erika.service to /etc/default/erika
```console
sudo cp default/erika.service /etc/default/erika
```

### adapt to local system

* you can set different serial ports and other options in /etc/default/erika
* you can adjust the virtual printer port in /var/lib/erika/setperm.sh

### test service

* start erika service
  * sudo systemctl start erika
* stop erika service
  * sudo systemctl stop erika
* get status of erika service
  * sudo systemctl status erika

### install service 

* enable service for default start
  * sudo systemctl enable erika
