class Employee :
    no_of_leaves = 8

    def __init__(self,aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"Name is : {self.name}\nSalary is : {self.salary}\nRole is : {self.role}"

    @classmethod
    def change_leaves(cls , newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other): # called dunder add - for help to operater overload
        '''Dunder or magic methods in Python are the methods having two prefix and suffix underscores
        in the method name. Dunder here means “Double Under (Underscores)”.
        These are commonly used for operator overloading.
        Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.'''

        return self.salary + other.salary

    def __repr__(self) : # str() and repr() both are used to get a string representation of object.
        '''repr() is mainly used for debugging and development. '''
        '''repr() compute the “official” string representation of an object 
        (a representation that has all information about the object) '''

        return f"Employee('{self.name}' , {self.salary} , '{self.role}')"

    def __str__(self) : # str() and repr() both are used to get a string representation of object.
        '''str() is used for creating output for end user '''

        '''str() is used to compute the “informal” string representation of an object 
        (a representation that is useful for printing the object).'''

        return f"Name is : {self.name}\nSalary is : {self.salary}\nRole is : {self.role}"

emp = Employee("Pratik" , 3545 , "Programmer")
# emp2 = Employee("niraj" , 4545 , "Cleaner")
print(emp)

''' str() is used for creating output for end user while repr() is mainly used for debugging and development. 
repr’s goal is to be unambiguous and str’s is to be readable. For example, if we suspect a float has a small rounding error, 
repr will show us while str may not.

repr() compute the “official” string representation of an object (a representation that has all information about the object) 
and str() is used to compute the “informal” string representation of an object (a representation that is useful for printing 
the object). '''
