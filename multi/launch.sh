#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/thesis-software/multi/
sudo python bg_test.py
cd /