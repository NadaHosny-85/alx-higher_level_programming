#!/usr/bin/python3
"""define a student class"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initializing the student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
