#!/usr/bin/env python

# https://adventofcode.com/2021/day/2
# What do you get if you multiply your final 
# horizontal position by your final depth?

x = z = 0

with open('input/02.txt') as file:
    while (line := file.readline().rstrip()):
        value = int(line[-1])
        if "forward" in line:
            x += value
        if "down" in line:
            z -= value
        if "up" in line:
            z += value

depth = abs(z)
total = x * depth
print(total)