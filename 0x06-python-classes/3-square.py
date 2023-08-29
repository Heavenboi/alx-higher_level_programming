#!/usr/bin/python3
"""
This function defines a Square Class.
"""


class Square:
    """
    Respresents a  square.
    """
    def __init__(self, size=0):
        """
        Intialise a square with a given size.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        This method returns the current square area
        """
        return self.__size ** 2
