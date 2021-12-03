n=int(input("enter a number "))
start=2
while(start<n):
    if(n%start==0):
        break
    else:
        start=start+1
if(start==n):
    print(n," is a prime number")
else:
    print(n," is not a prie number")
