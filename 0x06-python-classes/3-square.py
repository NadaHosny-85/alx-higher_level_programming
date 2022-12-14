#!/usr/bin/python3

"""this is a square class with its own attributes"""


class Square():
    """class square with its attribute size which must be an integer"""

    def __init__(self, size=0):
        """initializing the class"""

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method returns area of the current square"""

        return self.__size ** 2
