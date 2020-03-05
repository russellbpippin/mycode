#!/usr/bin/env python3

from subprocess import call

call(["ip", "linkl","show","up"])

print("this program will check your interfaces")

interface= input("enter an interface, like, ens3: ")
call(["ip","addr","show", "dev", interface])


