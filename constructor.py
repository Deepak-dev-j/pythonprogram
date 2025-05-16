
# # # # # # current object is denote using self keyword

# # # # # class laptop:
   
# # # # #     def __init__(self):
# # # # #         self.price=0
# # # # #         self.ram=""
# # # # #         print("demo")
# # # # #     def display(self):
# # # # #         print("display")

# # # # # hp=laptop()
# # # # # hp.price="500000"
# # # # # hp.ram="8gb"
# # # # # print(hp.price)
# # # # # print(hp.ram)
# # # # # hp.display()


# # # # # examples

# # # class student:
# # #     def __init__(self):
# # #         self.name="kjkhk"
# # #         self.reg_number="78"
# # #     def display(self):
# # #             print("name:",self.name)
# # #             print("reg_number:",self.reg_number)
              
                 
# # # s1=student()

# # # print(s1.name)
# # # print(s1.reg_number)
# # # s1.display()

# # class fruit:
# #     def __init__(self,col):
# #         self.color=col

# # apple=fruit("black")
# # print(apple.color)

# class teacher:
#     def __init__(self,name,reg):
#         self.name=name
#         self.reg=reg

#     def display(self):
#         print("name:",self.name)
#         print("reg:",self.reg)
    
# t1=teacher("thomas",1)
# t2=teacher("john",2)
# t1.display()
# t2.display()
        





class calculator():
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("self:",self.num1+self.num2)
a=input()
b=input()
a1=calculator(a,b)
a1.add()
        
        
