n=int(input("enter the number:"))
for i in range(0,n):
    
    for k in range(0,n-i-1):
        print(' ',end='')
    for j in range(0,i+1):
        print('* ',end='')
    print('')

for i in range(0,n):
        for k in range(0,i):
         print(' ',end='')
        for j in range(0,n-i):
         print('* ',end='')
        print('')
    

for i in range(0,n):
    for k in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('* ',end='')
    print('')
    
for i in range(0,n):
    for k in range(0,i):
        print(' ',end='')
    for j in range(0,n-i):
        print('* ',end='')
    print('')


# n=int(input("enter the number of N:"))

for i in range(0,n):
    for k in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('* ',end='')
    print('')