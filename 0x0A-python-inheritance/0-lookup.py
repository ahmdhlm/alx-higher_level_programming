#!/usr/bin/python3
"""
Module: 0-lookup
Find returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Function that returns the list of available attributes and methods of an ob    
    Args: 
        - obj is the object to look into
    Returns:
        list:list of attributes
    """

    return dir(obj)
