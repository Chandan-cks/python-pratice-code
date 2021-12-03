sum=0
avg=0
ctr=0
n=int(input("enter the number "))
#type1
while(n>=1):
    print(n)
    sum=sum+n
    n=n-1
    ctr=ctr+1
#type2
'''for n in range(n,0,-1):
    print(n)
    sum=sum+n
    n=n-1
    ctr=ctr+1'''
print("add all: ",sum)
print("average: ",sum/ctr)
