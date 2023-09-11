#!/usr/bin/python3
"""
a class that in iherits from list
"""


class MyList(list):
    """
    the clas that inherits from the list
    """
    def print_sorted(self):
        """
        a function tha sorts the list
        """
        sorted_list = sorted(self)
        print(sorted_list)
