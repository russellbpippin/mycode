#!/usr/bin/env python3


import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
lookfor = input("what am i looking for? ")
lookwhere = input("what is the path in which i should search? ")

print(find(lookfor, lookwhere))

