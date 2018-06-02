# Assignment: Checkerboard
# Karen Clark
# 2018-06-02

# Assignment: Checkerboard
# Write a program that prints a red 'checkerboard' pattern to the console.

from __future__ import print_function
from colorama import init, Fore
from termcolor import colored

def checkerboard():
    init()

    row_count = 0

    while row_count < 10:
        if row_count % 2 == 0:
            print(colored('* * * * * ', 'red'))
            row_count += 1
        else:
            print(colored(' * * * * *', 'red'))
            row_count += 1