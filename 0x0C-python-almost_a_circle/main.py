#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    # r1 = Rectangle(3, 5, 1)
    # r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12 })
    # print(r1)
    print(r2.to_dictionary())
    # print(r1 is r2)
    # print(r1 == r2)