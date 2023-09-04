#!/usr/bin/env python3
"""
Creates instances of the Rectangle class and prints their attribute dictionaries.
"""

class Rectangle:
    """
    Represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height


my_rectangle.width = 10
my_rectangle.height = 3

my_rectangle = Rectangle(2, 4)
