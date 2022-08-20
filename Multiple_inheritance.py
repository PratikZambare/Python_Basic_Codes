class Employee :
    no_of_leaves = 8
    var = 8

    def __init__(self,aname , asalary , arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"Name is : {self.name}\nSalary is : {self.salary}\nRole is : {self.role}"

    @classmethod
    def change_leaves(cls , newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
        return "Thenga"

class Player :
    no_games = 4
    var = 9
    def __init__(self ,game , name):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"The name is : {self.name}\n Game is : {self.game}"

class CoolProgrammer(Employee , Player) :
    var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)

pratik = Employee("Pratik","50000","Manager")
rohan = Employee("Niraj","60000","IIT Techinician")

shubham = Player("shubham",["Cricket"])
karan = CoolProgrammer("karan","50000","CoolProgrammer")

# det = karan.print_details()
# karan.printlanguage()
print(karan.no_of_leaves)