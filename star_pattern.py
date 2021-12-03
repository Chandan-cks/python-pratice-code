"""for i in range(0,10,1):
    for j in range(i+1,0,-1):
        print("*",end=" ")
    print()
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * *
"""
"""for i in range(0,10):
    
    for j in range(0,9-i):
        
        print(" ",end="")
    for c in range(0,i+1):
        print("*",end=" ")#give space for trangle pattern,no space for right side start star pattern
    print()
"""
for i in range(0,10):
    
    for j in range(0,9-i):
        
        print(" ",end=" ")
    for c in range(0,i+1):
        print(c+1,end=" ")#give space for trangle pattern,no space for right side start star pattern
    print()
