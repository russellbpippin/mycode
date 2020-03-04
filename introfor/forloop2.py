#!/usr/bin/env python3


vendors = ["cisco","juniper", "big_ip","f5","arista","alta3","zack","stuart"]

approved_vendors = ["cisco","juniper","big_ip"]

for x in vendors:
    print("\nThe vendo is " + x, end= " ")
    if x not in approved_vendors: 
        print("  _NOT AN APPROVED VENDOR", end=" ")

print("\nOur loop has ended")



