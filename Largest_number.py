#7.Python Program to Find the Largest number among Three Numbers
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if(a>b and a>c):
    print("a is largest number.",a)
elif(b>a and b>c):
    print("b is largest number.",b)
else:
    print("c is largest number.",c)
