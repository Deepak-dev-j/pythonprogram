class a:
    def __init__(self):
        print("a")
    def display(self):
        print("hello")


class b():
    def __init__(self):
        super().__init__()
        print("b")
    def display(self):
        print("hi")


class c(a,b):
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("namaskar")
obj1=c()

