class Employee :
    no_of_leaves = 8

    def __init__(self,aname , asalary , arole): # constructor called name __init__
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"Name is : {self.name}\nSalary is : {self.salary}\nRole is : {self.role}"

    @classmethod # class method accessed using def any_name (And here is "cls" not an self , or a extra variable)
    def change_leaves(cls , newleaves): #class method to change the class variable values though the object or class
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        return "Thenga"

class Programmer(Employee) : # Single level inehritance
    def __init__(self, aname , asalary , arole , languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"The Programmers name is : {self.name}\nSalary is : {self.salary}\nRole is : {self.role}\n And the languages are {self.languages}"


pratik = Employee("Pratik","50000","Manager")
rohan = Employee("Niraj","60000","IIT Techinician")
# karan = Employee.from_str("Karan-480-student")

shubham = Programmer("shubham","555","Programmer",["Python"])
karan = Programmer("Karan","777","Programmer",["Python","cpp"])
# print(pratik.print_details())
print(karan.printprog())