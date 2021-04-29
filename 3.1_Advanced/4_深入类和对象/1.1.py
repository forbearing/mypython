#!/usr/bin/env python3

class Cat(object):
    def say(self):
        print("I'm a cat")

class Dog(object):
    def say(self):
        print("I'm a dog")

class Duck(object):
    def say(self):
        print("I'm a duck")

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()
