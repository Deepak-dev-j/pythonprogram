def add_one(num):
    if (num>=9):
        return num+1
    total=num+1
    print(total)

add_one(7)

def fact(num):
    if (num==1):
            return 1
    else:
            return num*fact(num-1)
print(fact(int(input("enter the number:"))))