# # # # # # # # # factrorial numbers

# # # # # # # # def fact(x):
# # # # # # # #     if x==1:
# # # # # # # #         return 1
# # # # # # # #     else:
# # # # # # # #         return (x*fact(x-1))

# # # # # # # # num=5
# # # # # # # # print("the factorial is","is",fact(num))

# # # # # # # # lambda function

# # # # # # # # square=lambda x: (x**2)
# # # # # # # # print(square(6))


# # # # # # # # equilance to 'r' or 'rt'

# # # # # # # f=open("test.txt")
# # # # # # # f=open("test.txt",'w')
# # # # # # # f=open("test.txt",'r+b')
# # # # # # # f=open("test.txt",'txt')

# # # # # # # f=close("test.txt")

# # # # # # f=open("demofile.txt",'a')

# # # # # # f.write("now be wote")
# # # # # # f.close()

# # # # # f=open("demofile.txt",'r',encoding='utf-8')
# # # # # f.read(4)

# # # # # f.close()

# # # # import sys

# # # # # exception handling

# # # # randomlist=['a',0,2]

# # # # for entry in randomlist:
# # # #     try:
# # # #      print("the entry is entry",entry)
# # # #      r=1/int(entry)
# # # #      break
# # # #     except:
# # # #      print("oops!",sys.exc_info()[0],"occured")
# # # #      print("next entry")

# # # #      print()
# # # # print("the reciprocal of ",entry,"is",r)
     


# # # import os
# # # os.getcwd()  #present working directory
# # # os.chdir('D:\HELLO') #changing current directory
# # # os.listdir()#list al sub directories
# # # os.mkdir('test')#making a new directorty set
# # # os.rename('test','tasty')# remaining the directroy test to tasty
# # # os.remove('old.txt')#directing old.txt.file



# # class myclass:
# #   "This is my class"
# #   a=10
# #   def func(self):
# #     print("hello")
    

# # print(myclass.a)
# # print(myclass.func)
# # print(myclass.__doc__)


# # constructors

# class complexnumbers:
#     def __init__(self,r=0,i=0):
#         self.real=r
#         self.imag=i

#     def getData(self):
#         print("{0}+{1}d".format(self.real,self.imag))
# c1=complexnumbers(2,3)
# c1.getData()



#inheritance

class mamel:
    def displaymamelfeautures(self):
        print("mamels worm blood animals")

class dog(mamel):
    def displaydogfeautures(self):
        print("dog have four legs")

d=dog()
d.displaymamelfeautures()
d.displaydogfeautures()
