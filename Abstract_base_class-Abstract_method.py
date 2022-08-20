from abc import ABC , abstractmethod
class shape : # Abstract base class
    @abstractmethod # Abstract method is a method that set a rule for all child classes
    def print_area(self): # in this case the rule is every inherited class has compulsory a print area function.
        return 0

class rectangle (ABC): # inherited class of a base class shape
    type = "rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self): # compulsory fun set by a base class shape and a abstract class
        return self.length * self.breadth

print1 = rectangle()
print(print1.print_area())