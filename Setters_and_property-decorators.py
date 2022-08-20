
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

hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US" # changes the 1st name of the hindustani supporter

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com" # this line needs the property setter
print(hindustani_supporter.email)

del hindustani_supporter.email # this line uses the property deleter
print(hindustani_supporter.email)
hindustani_supporter.email = "harry.perry@pratik.com  " # calling setter after calling deleter
print(hindustani_supporter.email)

