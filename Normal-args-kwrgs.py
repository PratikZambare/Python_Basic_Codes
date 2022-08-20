# Tip :- any name is not compulsory in this program you can use anything you want

def funargs (normal , *args , **kwargs) : # received anything as a tuple
    print(normal,"\n")
    for item in args:
        print(f"this is in the args : {item}")
    print("\nsome persons and their qualities : ")
    for i , j in kwargs.items() :
        print(f"{i} is : {j}")


par = ["Pratik","Minal","Gunjan","Kunal","Mayuri","Nachiket"] # pass the whole string in a single argument
normal = "This is a normal argument : "
kwrgs = {"Pratik" : "Smart", "Minal" : " Hot" , "Gunjan" : "Sweet" , "Kunal" : "Nice"} # passing the dict in a single arugument
funargs(normal , *par , **kwrgs)