#!/bin/bash
killall conky
sleep 5
killall conky
conky -d -c /home/wido/.conky/.conkyrc;
#conky -d -c /home/wido/.conky/conkyarch;
#conky -d -c /home/wido/.conky/.conkyimage;
exit


