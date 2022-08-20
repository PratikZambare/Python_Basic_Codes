import random # built in module - use for random things
from PIL import Image # external module called pillow - used for open image


random_number = random.randint(0,1000)
print(random_number)
rand = random.random() * 1000
print(rand)
lst = ["Pratik","Minal","Gunjan","Kunal","Nachiket","Jahnvi","Nisha","Roshani","Aditya"]
choice = random.choice(lst)
print(choice)

im = Image.open("ybear.jpg")
im.show()
