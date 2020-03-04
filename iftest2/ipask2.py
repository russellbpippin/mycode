#!/usr/bin/env python3
  
ipchk = input("Apply an IP adress: ")

if ipchk == "192.168.70.1":
    print("looks like the ip address of the gatewas was set: " + ipchk + "This is not recommended.")
elif ipchk:
    print("Looks like the ip was set: " + ipchk)
else:
    print("You did not provide any input")


