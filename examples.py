a=[]
print("enter 6 numbers")
for i in range(6):
    num=int(input("enter the number"+str(i+1) +":"))
    a.append(num)
print(a)

sum=0
for i in a:
   sum=sum+i
   print(sum)


