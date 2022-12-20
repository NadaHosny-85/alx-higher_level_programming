#!/usr/bin/python3

"""this is a square class with its own attributes"""  


class Square():
    """class square with its attribute size which must be an integer"""

    def __init__(self, size=0, position=(0, 0)):
        """initializing the class"""

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """instance returns size itself"""

        return (self.__size)

    @size.setter
    def size(self):
        """set a new value for size and check on its if conditions"""

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieves the position value"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """set a new value for position and check on its conditions"""

        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((type(value[0]) is not int) or (type(value[1]) is not int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((value[0] < 0) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """prints our square using # special character"""

        if (self.__size == 0):
            print("")

        for i in range(self.__position[1]):
            print("")
        for x in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
            print("")
