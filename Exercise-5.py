import datetime
def partik(self):
    if self == 1:
        # n = str(input(" pratik or niraj : "))
        # if n == 'pratik' or 'Pratik':
        f = open("pratik.txt", "w")
        data = input("enter the food you eaten morning : ")
        f.write(str(datetime.datetime.now()) + " : " + str(data))
        f.close()
    elif self == 2:
        f = open("pratik.txt")
        print(f.read())


def niraj(self):
    if self == 1:
        data = input("enter the food you eatan morning : ")
        s = open("niraj.txt" , "w")
        s.write(str(datetime.datetime.now()) + " : " + str(data))
        s.close()
    elif self == 2:
            s = open("niraj.txt")
            print(s.read())
def main() :
    k1 = int(input(" Enter 1 for enter data and enter 2 for retrive data : "))
    k = int(input(" pratik or niraj : "))
    if k == 1 :
        partik(k1)
    if k == 2 :
        niraj(k1)
main()
l = input("Press Y or y to view entered data : ")
while (l == 'y' or 'Y') :
    main()
