# # # # list
# # # # set
# # # # dictionary
# # # # tuple


# # list using square brackets[]



# # # list=[1,2,3,4,"apple","apple"]
# # # print(list)
# # # list.append(7)
# # # print(list)
# # # list.insert(0,11)
# # # print(list)
# # # list[2]=11
# # # print(list)
# # # list.pop(5)
# # # print(list)

# # # b=[11,23,12]
# # # list.extend(b)
# # # print(list)



# # # tuple using parenthesis

# # a=(1,2,3,4,5)
# # print(a)
# # b=list(a)
# # print(b)
# # b[0]=10
# # print(b)


# # set collections using curly brackets{}
# # do not allow duplicate
# # sets unordered

# set={1,2,3,4,4,"apple","mango"}
# print(set)
# set.add(10)
# print(set)
# set.remove("mango")
# print(set)
# set,pop(1)



# dictionaries

# a={"name":"emc",
#    "age":1,
#  "location":"puthukottai",
#   "students":["bala","john"]
# }
# print(a.keys())
# print(a.values())
# a["age"]=2
# print(a)

numbers=range(1,6)
print(dict.fromkeys(numbers,99))