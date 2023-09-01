class MyClass:
    class_var = "Class-level Variable"

    def __init__(self):
        self.instance_var = "Instance-level Variable"

    def instance_method(self):
        return "Instance Method"

obj = MyClass()
class_attribute = getattr(obj, "class_var")
print(class_attribute)