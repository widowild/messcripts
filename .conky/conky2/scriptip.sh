#!/bin/bash
wget http://checkip.dyndns.org/ -O - -o /dev/null | cut -d: -f 2 | cut -d\< -f 1

