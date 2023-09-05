#!/usr/bin/python3

class Person:
	def __del__(self):
		print("Hello Egypt")

person = Person()
del person