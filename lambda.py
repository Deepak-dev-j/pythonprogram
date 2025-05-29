squared =lambda num: num*num
print(squared(5))


add=lambda num: num+2
print(add(2))

# two parameter

sum=lambda a,b:a+b
print(sum(1,2))


def funcbuild(x):
    return lambda num:num*x
func=funcbuild(2)
print(func(10))

# higher order function

numbers=[2,3,7,8,9,10]
squared=map(lambda num:num*num,numbers)
print(list(squared))

# filter

oddnum=filter(lambda num:num%2 != 0,numbers)
print(list(oddnum))