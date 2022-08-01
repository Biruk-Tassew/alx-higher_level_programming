#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """oposite version of an integer"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """swap != and now =="""
        return int(self) != other

    def __ne__(self, other):
        """swap == and now !="""
        return int(self) == other
