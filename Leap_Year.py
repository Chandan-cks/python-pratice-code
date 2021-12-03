#6.Python Program to Check Leap Year
year=int(input("enter a year: "))
if((year%400==0)or
    (year%4==0)):
    
        print("leap year")
else:
    print("not a leap year")
    
