# Create a class to model an object
class Example:
    def _init_(self, param_1):
        self.param1 = param_1

    def _str_(self):
        return """This is a return function when class is
            called in print statement."""

    def my_func(self):
        print("Code to Execute")


# Create new instance of object class
my_class_var = Example('Param1 Value')

# Call methods of instance
my_class_var.my_func()

# Print return string for instance
print(my_class_var)
