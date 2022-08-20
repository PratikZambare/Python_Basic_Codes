from PIL import Image # pip install PIL
print("What i look like program :")
name = input("Enter your name : ")
if name == 'niraj' :
    im = Image.open("ybear.jpg")
    im.show()