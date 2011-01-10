#!/bin/bash
#~/.bashrc
#export MPD_HOST="127.0.0.1"
#export MPD_PORT="6600"
#
killall mpd
touch /home/wido/.mpd/mpd.pid
mpd --no-daemon --verbose --stdout /home/wido/.mpd/config &
