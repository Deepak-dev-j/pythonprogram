# salary=int(input("enter your salary:"))
# age= int(input("enter your age:"))

# if salary>=20000 or age<=25:
#     loan=int(input("how much required loan amount:"))
#     if loan>50000 :
#         print("max loan amnt 50000")
#     else:
#         print("you are eligible for loan")
# else:
#     print("you not eligible for loan")

# ----------------------------

sub1=int(input("enter marks sub1:"))
sub2=int(input("enter marks sub2:"))
sub3=int(input("enter marks sub3:"))
sub4=int(input("enter marks sub4:"))
sub5=int(input("enter marks sub5:"))

avg= sub1+sub2+sub3+sub4+sub5/5

if avg<35:
    print("additional class required")
else:
    print("good to go")