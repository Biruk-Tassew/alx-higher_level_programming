#!/usr/bin/python3
class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'last_name'"""
    __slots__ = ['last_name']
