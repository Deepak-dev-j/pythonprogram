# # # class dad:
# # #     def phone(self):
# # #         print("dad phone")
# # # class mom():
# # #     def sweet(self):
# # #         print("moms sweet")
# # # class son(dad,mom):
# # #     def laptop(self):
# # #         print("my laptop")
# # # ram=son()
# # # ram.phone()
# # # ram.sweet()


# # # multilevel inheritance

# # class grandpa:
# #     def phone(self):
# #         print("grandpa phone")
# # class dad(grandpa):
# #     def money(self):
# #         print("dad money")
# # class son(dad):
# #     def laptop(self):
# #         print("my laptop")
# # ram=son()
# # d1=dad()
# # # ram.phone()
# # ram.money()
# # ram.laptop()
# # d1.phone()

# # hiarchical inheritance

# class dad():
#     def money (self):
#         print("dad money")
# class son1(dad):
#     pass
# class son2(dad):
#     pass
# class son3(dad):
#     pass

# s2=son2()
# s2.money()


# hybrid inheriance
class dad():
    def money (self):
        print("dad money")
class land():
    def important():
        print("iportant land")
class son1(dad,land):
    print("i am land")
class son2(dad):
    print("this my land")
class son3(dad):
    print("our land")

s1=son3()
s1.money()