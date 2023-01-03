#!/use/bin/python3
"""this class defines a rectangle"""


class Rectangle:
    """rectangle definition"""

    def __init__(self, width=0, height=0):
        """initialising a new rectangle height and width"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width of the rectangle"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """set a new value to the width of the rectangle"""

        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height of the rectangle"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """set a value to the height of the rectangle"""

        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""

        return (self.__width * self.__height)

    def parameter(self):
        """returns the parameter of the rectangle"""

        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))
