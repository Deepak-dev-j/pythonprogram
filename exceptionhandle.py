# # # compiletime error--syntax error
# # # logical error
# # # runtime error


# # # print("hi")
# # # print("bye")
# # # printt("hey")

# # # logical error
# # a=10
# # b=20
# # print(a+a)


# # runtime error
# try:
#     a=(input())
#     b=(input())
#     print(a/b)
# except Exception as e:
#     print("something wrong",e)

try:
    a=int(input())
    b=int(input())
    c=input()
    print(c/a)
    # print(d)
except  ValueError as e:
    print("valueerror",e)
except TypeError as e:
    print("typeerror",e)
finally:
    print("done")