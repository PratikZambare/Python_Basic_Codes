''' Object introspection means is to know about a object and know that which class is that object is coming from
    And what type of object is this and know to object id - every object has its own id. '''

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter # Use to set an attribute
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter # use to delete that attribute.
    def email(self):
        self.fname  = None
        self.lname  = None

Skillf = Employee("Skill", "F")
# print(Skillf.email)
print(type("This is a string"))
print(id("This is a string"))
o = "This is a string"
print(dir(0))