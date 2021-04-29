#!/usr/bin/env python3

# class Date:
    # def __init__(self, birth):
        # self.__birth = birth
    # def __get_birth(self):
        # return self.__birth

# d = Date(1996)
# #print(date.__birth)
# #print(date.__get_birth())
# print(d._Date__birth)
# print(d._Date.__get_birth())

class Date:
    def __init__(self,birthday):
        self.__birthday=birthday
    def __get_birthday(self):
        return self.__birthday
date=Date(1960)
print(date._Date__birthday)
print(date._Date__get_birthday())
