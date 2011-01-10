#!/usr/bin/env python
# -*- coding:utf8 -*-
#=================

from subprocess import call

import sys
import time

source, target = "/media/TERATOR/mirror", "root@192.168.0.10:/shares/mirror"
ssh = "'-e ssh -i /home/wido/.ssh/id_dsa'"
arguments = "-avz --delete-after"
rsync = "rsync"
cmd = "%s %s %s %s %s" % (rsync, arguments, ssh, source, target)

while True:
    ret = call(cmd, shell=True)
    if ret !=0:
        print("resubmitting rsync")
        time.sleep(30)
    else:
        print("rsync was successful")
        sys.exit(0)
