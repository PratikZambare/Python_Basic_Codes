class A :
    classvar1 = "I am a class variable in class A" # then final this
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance variable in class A" # instance variable then 2nd if not
        self.special = "Special"
class B (A):
    classvar1 = "I am class variable of class B" # then 3rd if not

    def __init__(self):

        self.var1 = "I am inside class B's constructor"
        super().__init__() # take the value from class a instance function
        self.classvar1 = "Instance variable in class B" # 1st if not

        # print(self.classvar1)
a=  A() # instances
b = B() # instances
print(b.special, b.var1 , b.classvar1)

'''An object is created and that call a variable in class child class
or a parent class if a instance varible is not available in b then it 
go to class a and find instance class if not found then find again in
class b but this time it will take a normal varible and if it also not
found then finf in class a # it is called an overiding'''