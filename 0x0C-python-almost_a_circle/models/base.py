#!/usr/bin/python3

class Base:
    """ Private class attribute __nb_objects
"""
    __nb_objects = 0
    """ class constructore """

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
