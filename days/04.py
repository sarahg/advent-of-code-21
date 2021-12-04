#!/usr/bin/env python

import sys
import numpy as np

# https://adventofcode.com/2021/day/4
# Bingo madness/something about a squid

def part_one(balls, cards):
    won, winners = set(), []

    # Create a matrix of all zeros for each card for marking.
    clean_cards = np.zeros_like(cards)

    for ball in balls:
        # Mark called balls on the empty card where they match a real card.
        clean_cards += (cards == ball)

        # Once a row/col has 5 values, it's a winner
        bingos = np.where((clean_cards.sum(axis=2) == 5) | (clean_cards.sum(axis=1) == 5))[0]

        # Add up the values in the winning row/col
        for i in bingos:
            if i not in won:
                won.add(i)
                winners.append((i, ball, clean_cards[i].copy()))

    # Unpack the first winner to solve.
    card_number, ball, mark = winners[0]
    
    # The solution for part 1 is:
    # the card index, times 
    # the sum of the unmarked numbers on the card, times 
    # the last ball called before the win.
    part_1 = (cards[card_number] * (1 - mark)).sum() * ball

    # Return the winning card value (solution for part 1)
    # and also the array of winners (needed for part 2)
    return part_1, winners


def part_two(winners, cards):
    """ 
    Given all the winners from part one,
    return the same solution but for the card that won last
    """
    ind, ball, mark = winners[-1]
    part_2 = (cards[ind] * (1 - mark)).sum() * ball
    return part_2


def main():
    data = open(sys.argv[1]).read()

    balls_str, cards_str = data.split('\n\n', maxsplit=1)
    balls = [int(x) for x in balls_str.split(',')]
    cards = np.array([int(x) for x in cards_str.split()]).reshape(-1, 5, 5)

    solution_one, winners = part_one(balls, cards)
    print(solution_one)

    print(part_two(winners, cards))


if __name__ == '__main__':
    main()