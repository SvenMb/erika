### Install erika service

#### manual installation from https://git.muehlbergnet

1. extract certificate for git.muehlberg.net:  
```
echo -n \\ | openssl s_client -showcerts -connect git.muehlberg.net:443 \\
2>/dev/null  | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' \\
> mbnet_cert.pem
```
2. add the cert to your git config  
`git config --global http."https://git.muehlberg.net:443/".sslCAInfo mbnet_cert.pem`
3. clone project directory  
`git clone https://git.muehlberg.net/SvenMb/erika.git`
4. change to project directory  
`cd erika`
5.  install python-evdev  
`sudo pip3 install evdev`
6.  copy src to /var/lib/erika  
`sudo cp -R src /var/lib/erika`
7. copy service/erika.service to /etc/systemd/system/erika.service  
`sudo cp service/erika.service /etc/systemd/system/erika.service`
8. copy default/erika.service to /etc/default/erika  
`sudo cp default/erika.service /etc/default/erika`

### adapt to local system

* you can set different serial ports and other options in /etc/default/erika
* you can adjust the virtual printer port permission and name in /var/lib/erika/setperm.sh

### test service

* start erika service  
  `sudo systemctl start erika`
* stop erika service  
  `sudo systemctl stop erika`
* get status of erika service  
  `sudo systemctl status erika`

### enable service for autostart 

* enable service for default start  
  `sudo systemctl enable erika`
