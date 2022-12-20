#!/usr/bin/python3

"""this is a square class with its own attributes"""


class Square():
    """class square with its attribute size which must be an integer"""

    def __init__(self, size=0):
        """initializing the class"""

        self.__size = size

    @retrieve_size
    def size(self):
        """instance returns size itself"""

        return self.__size

    @set_size
    def size(self, value):
        """set a new value for size and check on its if conditions"""

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of the square"""

        return self.__size ** 2
