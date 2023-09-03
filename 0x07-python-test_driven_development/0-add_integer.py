#!/usr/bin/python3
""" 
Function that adds two numbers
The function retuns error if a or b is not an int or float
It returns an integer: the addition of a and b
"""
def add_integer(a, b=98):
    """
    Adds two integers and returns the result.
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")

    return int(float(a)) + int(float(b))
