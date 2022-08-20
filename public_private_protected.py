class Employee :
    no_of_leaves = 8
    _protected = 89
    __private = 98

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


pratik = Employee("Pratik","50000","Manager")
# print(pratik._protected)
# print(pratik.__private)
# print(pratik._Employee__private)
class test :
    # pratik = Employee("Pratik", "50000", "Manager")
    # print(pratik._protected)
    print(pratik.printgood("Niraj"))