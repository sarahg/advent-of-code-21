#!/usr/bin/env python

import pandas as pd

# https://adventofcode.com/2021/day/3
# Use the binary numbers in your diagnostic report to 
# calculate the gamma rate and epsilon rate, then multiply them together.
# What is the power consumption of the submarine?

columns = 12

# Generate the gamma rate by finding the most common bit 
# in the corresponding position.

# Create a dataframe from the text file.
df = pd.read_csv('input/03.txt', sep="\n", header=None, dtype = str)

# Create a column for each bit.
df_cols = df[0].str.split("", expand=True)

x = 1
gammaBinary = ""
while x <= columns:
    value = int(df_cols[x].mode())
    gammaBinary += str(value)
    x += 1

gamma = int(gammaBinary, 2)

# Generate epsilon rate.
# Rather than use the most common bit, it's the least common bit.

epsilonBinary = ""
for bit in gammaBinary:
    if bit == "0":
        epsilonBinary += "1"
    if bit == "1":
        epsilonBinary += "0"

epsilon = int(epsilonBinary, 2)

# Calculate the total power consumption.
power = gamma * epsilon
print(power)