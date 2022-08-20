import fileinput

f = open("pratik.txt")
print(f.readline())
print("At this number : " , f.tell() , "\n") # TO TELL  THAT WHERE IS POINTER NOW IN FILE
print(f.readlines()) # print all lines in a list manner
# print(f.readline()) # READ LINE BY LINE
# print(f.seek(25)) # GO TO SPECIFIC POINTER
# print(f.readline())
f.close()