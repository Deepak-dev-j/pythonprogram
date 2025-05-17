from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def moveforward(self):
        pass
    
    def movebackward(self):
        print("hello")
   
    def fm(self):
        pass

class benz(Car):
    def moveforward(self):
        print("Swift is moving forward")
    def movebackward(self):
        print("swift car move backward")

b1=benz()
b1.movebackward()