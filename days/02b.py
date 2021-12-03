#!/usr/bin/env python

# https://adventofcode.com/2021/day/2
# What do you get if you multiply your 
# final horizontal position by your final depth?

x = z = aim = 0

with open('input/02.txt') as file:
    while (line := file.readline().rstrip()):
        value = int(line[-1])
        if "forward" in line:
            x += value
            z += aim * value
        if "down" in line:
            aim += value
        if "up" in line:
            aim -= value

print(x * z)