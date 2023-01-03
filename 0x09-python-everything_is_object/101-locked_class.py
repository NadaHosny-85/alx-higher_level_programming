#!/usr/bin/python3
"""class that prevents the user from dynamically creating new instance attributes"""


class LockedClass():
    """preventing dynamic attributes"""

    __slots__ = ['first_name']

    def __init__(self):
        """initialising class"""

        pass
