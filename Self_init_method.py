class Employee :
    no_of_leaves = 8
    def __init__(self,aname , asalary , arole): # constructor called name __init__
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"Name is : {self.name}\nSalary is : {self.salary}\nRole is : {self.role}"

pratik = Employee("Pratik","50000","Manager")
rohan = Employee("Niraj","60000","IIT Techinician")

# pratik = Employee()
# niraj = Employee()
# pratik.name = "patrick"
# pratik.salary = 50000
# pratik.role = "manager"
# niraj.name = "panda"
# niraj.salary = 66000
# niraj.role = "IIT techinical"

print(pratik.role)