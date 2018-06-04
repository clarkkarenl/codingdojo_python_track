# Assignment: Coin Tosses
# Karen Clark
# 2018-06-03

import random

# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
def coin_tosses():

    def toss(n, coin, count_heads, count_tails):
        print "Attempt #" + str(n) + ": Throwing a coin... It's a " + coin + "! ... Got " + str(count_heads) + " head(s) so far and " + str(count_tails) + " tail(s) so far"

    count_heads = 0
    count_tails = 0

    for i in range(1, 5001):
        n = i

        toss_value = random.randint(1, 101)
        if toss_value < 51:
            coin = 'head'
            count_heads += 1
        elif toss_value > 50:
            coin = 'tail'
            count_tails += 1
        toss(n, coin, count_heads, count_tails)

    print "Ending the program, thank you!"
    return