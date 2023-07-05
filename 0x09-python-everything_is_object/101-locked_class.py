#!/usr/bin/python3
"""

prevents the user from dynamically creating new inst

"""


class LockedClass:

    __slots__ = ['first_name']

    def __init__(self):
        """ Init method
        """
        pass
