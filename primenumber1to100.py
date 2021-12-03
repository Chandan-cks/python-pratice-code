#wap in python to display all prime no between 1 to 100
"""n=1
while(n<=100):
    start=2
    m=n
    while(start<=m):
        if(m%start==0):
            break
        else:
            start=start+1
        if(start==m):
            print(m)
    n=n+1
    """
"""for i in range (1, 101):
    
    for i in range(2, (i//2 + 1)):
        if(i % i == 0):
            count = count + 1
            break

    if (count == 0 and i != 1):
        print(i)"""
x = 1
y= 100
for num in range(x,y + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
