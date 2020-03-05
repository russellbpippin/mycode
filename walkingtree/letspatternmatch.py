#!/usr/bin/env python3

import os

import fnmatch

EXCLUDE = ["/usr","/home","/var"]

def find(pattern, path):
    result = []
    for root in os.walk(path, topdown=True):
        if root in EXCLUDE:
            root[:] = []
            root[:] = []
        for name in root:
            if fnmatch.fnmatch(name,pattern):
                result.append(os.path.join(root,name))
    return result

def main():
    lookfor = input("what pattern am i looking for (example: *.txt or *.cfg)? ")
    lookwhere = input("what is the path in which i should search? ")
    print("results: ", find(lookfor, lookwhere))

main()



