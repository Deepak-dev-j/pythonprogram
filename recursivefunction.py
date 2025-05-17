# # # # like a for loop

# # # def cook(balance_maavu):
# # #     if balance_maavu==1:
# # #        return 1
# # #     else:
# # #         total_vadai=1+cook(balance_maavu-1)
# # #         return total_vadai
    
# # # total_vadai=cook(4)
# # # print("take this",total_vadai,"vadai")


# # def cook(balance_maavu):
# #     if balance_maavu==1:
# #         return 1
# #     else:
# #         totalvadai=1+cook(balance_maavu-1)
# #         return totalvadai
# # totalvadai=cook(4)
# # print(totalvadai)

# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return (x*fact(x-1))
# print(fact(int(input("enter the number:"))))


def fact(x):
    if x==1:
        return 1
    else:
        return (x*(fact(x-1)))
print(fact(int(input("ener the number:"))))