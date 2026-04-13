This repo contains a Python script that retrieves the IP address of a Jetson at boot time. See the installation instructions below to run it at boot. It keeps trying until it gets a valid IP address, then opens the serial connection to the Waveshare robot base, updates the OLED, closes the connection, and exits.

## Installation
1. Create a service file:
```bash
sudo nano /etc/systemd/system/myscript.service
```

2. Paste this:
```
[Unit]
Description=My Python Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/oled_ip.py
Restart=always
User=<your_username>

[Install]
WantedBy=multi-user.target
```
Make sure to replace your_username.   
3. Enable and start it:
```bash
sudo systemctl daemon-reload
sudo systemctl enable myscript
sudo systemctl start myscript
```
If you want to disable it:
```bash
sudo systemctl disable myscript
```