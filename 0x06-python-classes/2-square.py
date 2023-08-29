#!/usr/bin/python3
"""
this class defines a square.
"""


class Square:
    """
    represents a square hape
    """
    def __init__(self, size=0):
        """
        initialise a square with a given size.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be initger")
        elif size < 0:
            raise ValueError("must be >= 0")
