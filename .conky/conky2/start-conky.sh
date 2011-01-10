#!/bin/bash
sleep 1
killall conky
sleep 2
conky -d -c ~/.conky/conky2/conky1;
conky -d -c ~/.conky/conky2/conky2;
conky -d -c ~/.conky/conky2/conky3;
conky -d -c ~/.conky/conky2/conky4;
exit

