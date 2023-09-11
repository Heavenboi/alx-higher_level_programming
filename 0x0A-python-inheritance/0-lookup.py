#!/usr/bin/python3

"""
a fuction that returns a list of available attributes of an object
"""


def lookup(obj):
    """
    the function that returns the attrubutes of the object
    """
    return dir(obj)
