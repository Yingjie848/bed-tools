#!/usr/bin/python

from sys import argv
import os

file = argv[1]

f = open(file,'r')
chr = ""
end = 0
n = 0

for line in f:
    n += 1
    line.strip()
    ln = line.split()

    if n > 1 and ln[0] == chr :
        distance = int(ln[1]) - int(end)
        print "%s\t%s\t%s\t%s" % (ln[0],ln[1],ln[2],str(distance))

    chr = ln[0]
    end = ln[2]

