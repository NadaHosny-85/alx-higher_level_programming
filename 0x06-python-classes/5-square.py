#!/usr/bin/python3

"""this is a square class with its own attributes"""


class Square():
    """class square with its attribute size which must be an integer""" 

    def __init__(self, size=0):
        """initializing the class"""

        self.__size = size

    @property
    def size(self):
        """instance returns size itself"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """set a new value for size and check on its if conditions"""

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """prints our square using # special character"""

        if (self.__size == 0):
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
