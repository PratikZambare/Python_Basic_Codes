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

pratik = Employee("Pratik","50000","Manager")
rohan = Employee("Niraj","60000","IIT Techinician")
print(pratik.no_of_leaves)
# Employee.no_of_leaves = 89 # instance variable

# Employee.change_leaves(45) # also change using the class name
pratik.change_leaves(34) # changes the no_of_leaves through the pratik object
print(pratik.no_of_leaves)