# Assignment: Fun with Functions
# Karen Clark
# 2018-06-03

# Assignment: Fun with Functions
# Create a series of functions based on the below descriptions.

# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
def odd_even():
    for x in range(1, 2001):
        if x % 2 != 0:
            print "Number is " + str(x) + ". This is an odd number."
        else:
            print "Number is " + str(x) + ". This is an even number."


# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
# The function should multiply each value in the list by the second argument
def multiply(list_in, multiplier):
    new_list = list()
    for i in list_in:
        if isinstance(i, int) or isinstance(i, float) or isinstance(i, long) or isinstance(i, complex):
            new_list.append(i * multiplier)
        else:
            print "List must contain only numbers"
            exit()

    return new_list


# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list.

def layered_multiples(fun):
    outer_list = []
    for i in fun:
        inner_list = []
        n = 0
        while n < i:
            inner_list.append(1)
            n += 1
        outer_list.append(inner_list)
    return outer_list
