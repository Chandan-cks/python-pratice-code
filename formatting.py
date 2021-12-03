"""#formatting the output in python
in python output can be formatted by using place holder
print("%<type of info to display>" %<source of the info to display>)
example:
    rollno=int(input("enter a roll no: "))#101
    mark=float(input("enter marks: "))#78.65
    branch=input("enter branch name: ")#"Comp.sc"
    print("Roll no=%d",%rollno)
    print("marks secures=%f"%mark)
    print("branch=%s"%branch)
"""
num=int(input("enter a number "))
for n in range(1,10):
    print("%d * %d =%d"%(num,n,num*n))

#total no of format specifier /place holder within the string must be equal to total no of variables in the variable list.
