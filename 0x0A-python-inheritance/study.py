#!/usr/bin/python3

class Study:
    def __init__(self, count, name = "Mohamed"):
        self.count = count
        self.name = name

    def __str__(self):
        return str(self.count)
    def __add__(self, other):
        return self.count + other.count
    def __eq__(self, other):
        return self.count == other.other
    def __lt__(self, other):
        return self.count < other.count
    def __radd__(self, other):
        return self.count + other
    def __iadd__(self, other):
        self.count += (other.count * 30)
        return self.count
    def __pos__(self):
        return -self.count
    def __neg__(self):
        return self.count * 10
    def __invert__(self):
        return self.count * 400
    def __repr__(self):
        return f"Study({self.count})" 
    def __contains__(self, item):
        return item in self.name
s1 = Study(10)
s2 = Study(20)
# print(+s1)
# print(-s1)
# print(~s1)
# print(repr(eval(repr(s1))))
a = "Mohamedd" in s1
print(a)