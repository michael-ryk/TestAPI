class MyClass:
    def my_method(self):
        print("This is a method of", self)
obj = MyClass()
obj.my_method()  # `self` refers to `obj`