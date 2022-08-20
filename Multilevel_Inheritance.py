class Dad :
    basketball = 1
class Son(Dad) :
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"
class g_son (Son):
    dance = 6
    guitar = 1

    def isdance(self):
        return f"Yes I dance very awesomely {self.dance} no of times"

daddy = Dad()
Larry = Son()
harry = g_son()

print(harry.guitar)