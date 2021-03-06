#!/bin/env python3

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        if not isinstance(self, value):
            raise TypeError('Expected a string')
        self._first_name = value
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")
