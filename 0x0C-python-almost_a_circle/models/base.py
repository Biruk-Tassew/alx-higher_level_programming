#!/usr/bin/python3
"""
This module contains the "Base" class
"""

class Base:
    """The base class"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Init the class"""
        if id:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
