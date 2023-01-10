#!/usr/bin/python3
"""defines a class which represents a student"""


class Student:
    """the student representation"""

    def __init__(self, first_name, last_name, age):
        """initializing the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""

        if ((type(attrs) == list) and
                (all(type(ele) == str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return (self.__dict__)
