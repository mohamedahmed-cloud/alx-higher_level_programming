- Static method and Class method and object method
```py
@staticmethod
# didn't take any class or object as a first argument
def static(attr1, attr2):
	pass

@classmethod
# first attribute is class itself
def classMethod(cls, attr1):
	pass

# first attribute is object[instance] itself.
def objectMethod(self, attr2):
	pass
```