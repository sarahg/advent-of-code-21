#!/usr/bin/env python

# https://adventofcode.com/2021/day/1
# Count the number of times a depth measurement increases from the previous measurement.
# But this time, consider the sum of each set of 3 lines as a set, and compare those (sliding windows).

from numpy import loadtxt

depths = loadtxt("input/01.txt")

x = 0
sums = {}
while x < len(depths):
    window = depths[x:x+3]
    if len(window) == 3:
        sums[x] = sum(window)
    x += 1

higherDepthCount = 0

numList = list(sums.values())
i = 0
while i < len(numList):
    if numList[i] > numList[i - 1]:
        higherDepthCount += 1
    i += 1

print(higherDepthCount)