#!/usr/bin/python3
"""
Student class
"""


class Student:
    """
    class have not any args
    """
    def __init__(self, first_name, last_name, age):
        """
        method : __init
        args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return:
            that retrieves a dictionary
            representation of a Student instance
        """
        res = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        if attrs is None:
            return res
        else:
            return {attr: res.get(attr) for attr in attrs
                    if res.get(attr) is not None}
