# Assignment: Draw Stars
# Karen Clark
# 2018-06-04

# Assignment: Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and 
# prints out *.

from __future__ import print_function
from colorama import init, Fore
from termcolor import colored

def draw_stars(x):
    init()

    for i in range(len(x)):
        output = ""
        counter = x[i]
        while counter > 0:
            output += "*"
            counter -= 1

        print(colored(output, 'red'))

# Part II
# Modify the function above. Allow a list containing integers and strings 
# to be passed to the draw_stars() function. When a string is passed, 
# instead of # displaying *, display the first letter of the string 
# according to the # example below. 
def draw_stars2(x):
    init()
    
    for i in range(len(x)):
        output_int = ""
        output_str = ""
        first_letter = ""

        if isinstance(x[i], int):
            count_int = x[i]
            while count_int > 0:
                output_int += "*"
                count_int -= 1

            print(colored(output_int, 'red'))

        elif isinstance(x[i], str):
            first_letter = x[i][0].lower()
            count_str = len(x[i])
            while count_str > 0:
                output_str += first_letter
                count_str -= 1
            print(output_str)
