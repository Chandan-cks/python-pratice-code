#input details of a student
print("Enter rollno of a student:")
rollno=input()
print("Enter Student Name:")
name=input()
print("Enter 5 marks of a student:")
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
print("rollno", rollno)
print("Name", name)
sum = m1+m2+m3+m4+m5
print("Total marks", sum)
avg = int(sum/5)
print("Average marks of students", avg)
