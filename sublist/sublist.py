"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        return are_equal(list_one, list_two)
    
    if len(list_one) < len(list_two):
        return {True: SUBLIST, False: UNEQUAL}.get(is_in(list_one, list_two))
    
    return {True: SUPERLIST, False: UNEQUAL}.get(is_in(list_two, list_one))
    

def are_equal(list_one, list_two):
    if len(list_one) != len(list_two):
        return UNEQUAL
    for index, value in enumerate(list_one):
        if value != list_two[index]:
            return UNEQUAL
        
    return EQUAL

def is_in(list_one, list_two):
    if len(list_one) == 0: return True

    difference = len(list_one)
    for left_index in range(len(list_two) + difference):
        if are_equal(list_one, list_two[left_index:left_index + difference]) == EQUAL:
            return True

    return False
