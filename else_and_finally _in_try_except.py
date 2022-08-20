
f1 = open("pratik.txt")
try:
    f= open("does.txt")

except Exception as e :
    e

else:
    print("this messege you got if the except can't run")

finally:
    f1.close()
    print("Bhaay kuch run ho yaa naa ho ye to print karna hi he")

print('Important message')