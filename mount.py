#!/usr/bin/env python
 
import os
 
iso_file = os.popen("zenity --file-selection").read().strip()
if not iso_file: exit(0)
 
mount_point=os.popen("zenity --file-selection --directory").read().strip()
if not mount_point:
        print "Error: Mount point not specified"
        exit(-1)
        
mount_command = 'mount -o loop "%s" "%s"'% (iso_file, mount_point)
print(mount_command)
 
result = os.system(mount_command)
if result!=0:
        print "Error: Couldn't mount ISO file"
