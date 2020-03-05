#!/usr/bin/env python3
configfile = open("vlanconfig.cfg", "r")

configblog = configfile.read()

configlist = configblog.splitlines()
#configfile = open("vlanconfig.cfg", "r")

#configlist = configfile.readlines()
print(configlist)
#for x in configlist:
   # print(x)
configfile.close()
