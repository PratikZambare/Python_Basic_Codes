import time
init = time.time()
print(init)
k = 0
while (k<10) :
    print("Pratik is a good boy : ")
    k+=1
print(f"while loop completed in -- {time.time()-init} -- seconds")

print("\n")

init2 = time.time()
for i in range(10) :
    print("Pratik is a good boy : ")
print(f"for loop completed in -- {time.time()-init2} -- seconds")

# localtime = time.asctime()
# print(localtime)