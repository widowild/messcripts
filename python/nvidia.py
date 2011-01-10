#!/usr/bin/env python3

# affiche les données des GPU nvidia
# nvidia-smi -a
# Two Sli
import subprocess
import os


subprocess.Popen(["nvidia-smi","-a"], stdout=open("/home/wido/nvidia.log", "w"), stderr=open("/home/wido/nvidia.log", "w"))

fichier = open('/home/wido/nvidia.log',"r")
for ligne in fichier:
    if "Temperature" in ligne:
        line = ligne.split()
        print("Temperature:",line[-2])

    if "Fan Speed" in ligne:
        line = ligne.split()
        print("Fan Speed :",line[-1])
os.remove("/home/wido/nvidia.log")
