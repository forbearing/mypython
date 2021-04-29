#!/usr/bin/env python3

class Data:
    def __init__(self, year, month, day):                       # __init__ 实例方法
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,    # __str__ 实例方法
                month=self.month, day=self.day)
    def tomorrow(self):
        self.day += 1
    @staticmethod
    def parse_from_string(data_str):
        year, month, day = tuple(data_str.split('-'))
        return Data(int(year), int(month), int(day))

if __name__ == "__main__":
    new_day = Data(2020, 2, 27)
    new_day.tomorrow()
    print(new_day)
    data_str = "2020-2-27"
    new_day = Data.parse_from_string(data_str)
    print(new_day)
