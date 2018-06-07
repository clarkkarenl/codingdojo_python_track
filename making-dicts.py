# Assignment: Making Dictionaries
# Karen Clark
# 2018-06-06

# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a 
# single dictionary. The first list contains keys and the 
# second list contains the values. Assume the lists will 
# be of equal length.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    new_dict.update(zip(list1, list2))
    return new_dict

# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used 
# for the keys, the shorter for the values.

def make_dict_2(list1, list2):
    new_dict = {}
    if len(list1) == len(list2) or len(list1) > len(list2):
        new_dict.update(zip(list1, list2))
    elif len(list2) > len(list1):
        new_dict.update(zip(list2, list1))

    return new_dict
