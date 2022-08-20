lst = ["Pratik","Minal","Gunjan","Kunal","Nachiket","Jahnvi","Nisha","Roshani","Aditya"]
lst2 = ["Pratik","Minal","Gunjan","Kunal","Nachiket","Jahnvi","Nisha","Roshani","Aditya"]

for item in lst :
    print(item , end=" , ")    # simple form
print("are the classmates .")

a = " , ".join(lst)     # Using join function
print(f"{a} , are the classmates . ")