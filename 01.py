#!/usr/bin/env python

# https://adventofcode.com/2021/day/1
# Count the number of times a depth measurement increases from the previous measurement.

from numpy import loadtxt

depths = loadtxt("input/01.txt")

higherDepthCount = 0

for index, x in enumerate(depths):
    if x > depths[index - 1]:
        higherDepthCount += 1

print(higherDepthCount)