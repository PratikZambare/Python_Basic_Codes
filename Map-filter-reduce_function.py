# numbers = ["3","7","65"]
#
# numbers = list(map(int, numbers))
# numbers[1] = numbers[1] + 2
# print(numbers[1])

#--------------------------------MAP----------------------------------- # add given number in a list

# for i in range (len(numbers)) :   # Loop for treat character as integer and addtion of
#     numbers [i] = int(numbers[i]) # of a number and print that position number
# numbers[2] = numbers[2] + 2
# print(numbers[2])
# print(type(numbers[2]))
# #
# num = (1,2,3,4,5,6,7,8,9)
# # print(type(num))
# square = tuple(map(lambda x : x*x, num))
# # print(type(square))
# print(square)
# # print(num)

#------------------------------filter------------------------------ # return big number by given condition
# lst = [1,2,3,4,5,6,7,8,9]
#
# def is_greater_5(num):
#     return num>5
#
# fil = list(filter(is_greater_5 , lst))
# print(fil)

#------------------------------Reduce------------------------------ # add all numbers
#
# from functools import reduce
#
# list1 = [1,2,3,2,12,2]
# num = reduce(lambda x,y : x+y , list1)
# print(num)