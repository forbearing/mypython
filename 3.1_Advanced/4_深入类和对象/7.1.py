#!/usr/bin/env python3

class Date:
    def __init__(self, birth):
        self.__birth = birth
        self.name='hyb'
    def get_birth(self):
        return self.__birth

date = Date(1997)
#print(date.__birth)
print(date.get_birth())
