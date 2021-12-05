import numpy as np
import sys

#Part 1

#depth = 0
#hori = 0
#
#with open('input.txt') as f:
#    for line in f:
#        line2 = line.split()
#        if line2[0] == "down":
#            depth += int(line2[1])
#        elif line2[0] == "up":
#            depth -= int(line2[1])
#        elif line2[0] == "forward":
#            hori += int(line2[1])
#
#print(hori*depth)

#Part 2

depth = 0
hori = 0
aim = 0

with open('input.txt') as f:
    for line in f:
        line2 = line.split()
        instruc = line2[0]
        value = int(line2[1])
        if instruc == "down":
            aim += value
        elif instruc == "up":
            aim -= value
        elif instruc == "forward":
            hori += value
            depth += aim*value

print(hori*depth)

