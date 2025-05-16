# # class shape():
# #     def area(self):
# #         return 0
    
# # class rectangle(shape):
# #     def area(self):
# #         l=10
# #         b=20
# #         print(l*b)


# # s1=rectangle()
# # s1.area()


# class person():
#     def __init__(self,name):
#         self.name=name

# class student(person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade
       
#     def display(self):
#         # super().__init__()
#         print(self.name,self.grade)

# s1=student("john","a")
# s1.display()

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print(self.name + self.salary + self.department)
m1=manager("john","20000","it")
m1.display()
