class Employee :
    no_of_leaves = 8
    pass
pratik = Employee()
niraj = Employee()
pratik.name = "patrick"
pratik.salary = 50000
pratik.role = "manager"
niraj.name = "panda"
niraj.salary = 66000
niraj.role = "IIT techinical"

Employee.no_of_leaves = 7 # changes the class attributes
print(pratik.no_of_leaves)
print(niraj.__dict__) # __dict__ fuction to print the all attributes in dict.
niraj.no_of_leaves = 9 # changes the no of leaves only for the rohan.
print(niraj.__dict__)
print(Employee.no_of_leaves)