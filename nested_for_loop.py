"""n=int(input("enter a number "))
name=input("enter your name")
for r in range(1,n+1):
    for r in range(1,r+1):
        print(name,end="")
    print()
"""
n=int(input("enter a number "))
#name=input("enter your name")
for r in range(n,0,-1):
    for i in range(1,r+1,1):
        print(name,end=" ")
    print()
