#!/usr/bin/env python

import sys

# Pass the input file in as an argument.
file = open(sys.argv[1]).read().splitlines()

# https://adventofcode.com/2021/day/3
# Use the binary numbers in your diagnostic report to find
# the oxygen generator and co2 scrubber numbers, then multiply these.

def get_rating(fn_bit_criteria):
    numbers = file[:]
    bit = 0

    while len(numbers) > 1:
        zero = [number for number in numbers if number[bit] == "0"]
        one = [number for number in numbers if number[bit] == "1"]
        numbers = fn_bit_criteria(zero, one)
        bit += 1

    # Convert the binary into decimal on return.
    return int(numbers[0], 2)

# Pass bit criteria functions as lambdas
oxygen_generator = get_rating(lambda zero, one: one if len(one) >= len(zero) else zero)
co2_scrubber = get_rating(lambda zero, one: zero if len(one) >= len(zero) else one)

print(oxygen_generator * co2_scrubber)