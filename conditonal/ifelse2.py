# # a=int(input("enter the number:"))

# # if a%2==0:
# #     print("number is even")
# # else:
# #     print("number is odd")
# # --------------------------

# score=int(input("enter your score:"))

# if score<35:
#     print("poor student")
# elif 35<score and 70>score:
#     print("average student")
# elif score>70 and 100>=score :
#     print("Good student")

# elif score>100:
#     print("enter correct marks")

# ---------------------------------------

# make calci_______

a=int(input("enter your num1:"))
b=int(input("enter your num2:"))

operation =input("add/sub/mul/div:")
if(operation=="add"):
    print(a+b)
elif operation=="sub":
    print(a-b)
elif operation=="mul":
    print(a*b)
elif operation=="div":
    print(a/b)

else:
    print("invalid operation")
