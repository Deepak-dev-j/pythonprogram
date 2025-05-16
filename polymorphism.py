# def add(a,b,c=0):
#     print(a+b+c)
# add(1,2)
# add(1,2,3)


class animal():
    def sound(self):
        print("animal make sound")
class dog(animal):
    def sound(self):
        print("dog is barking")
class bird(animal):
    def sound(self):
        print("bird singing")
d1=bird()
d1.sound()
b1=dog()
b1.sound()