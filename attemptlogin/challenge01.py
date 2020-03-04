#!/usr/bin/env python3

loginsuccess = 0

keystone_file = open("keystone.common.wsgi","r")

keystone_file_lines = keystone_file.readlines()

for line in keystone_file_lines:
    if"- - - -] Authorization failed" in line:
        loginsuccess += -1
    if"- - - -] " and str() in line:
        loginsuccess += 1
print("The number of successful login attempts is: ", loginsuccess)
keystone_file.close()
