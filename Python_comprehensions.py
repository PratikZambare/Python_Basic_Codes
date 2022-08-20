# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# ls = []
# for i in range (100):
#     if i%3 == 0:
#         print(i)
#
# print(ls)

# ls = [i for i in range (100) if i%3 == 0] # list comprehentions

dict = {i:f"item{i}" for i in range(5)} # dict comprehentions
dict1 = {value:key for key,value in dict.items()} # change the pattern of storing.
print(dict,"\n",dict1)