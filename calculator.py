#Calculator
def add():
    a= float(input("Enter the 1st number = "))
    b= float(input("Enter the 2nd number = "))
    res= a + b
    print("the addition is ",res)

def sub():
    a= float(input("Enter the 1st number = "))
    b= float(input("Enter the 2nd number = "))
    res= a - b
    print('The result is ',res)

def mul():
    a= float(input("Enter the 1st number = "))
    b= float(input("Enter the 2nd number = "))
    res= a * b
    print('The result is ',res)

def div():
    a= float(input("Enter the 1st number = "))
    b= float(input("Enter the 2nd number = "))
    res= a / b
    print('The result is ',res)

while True:
    choice= input("1. Add 2. Subtract 3. Multiply 4. Divide 5. Exit\n")
    if choice == '1':
        add()
    elif choice=='2':
        sub()
    elif choice=='3':
        mul()
    elif choice=='4':
        div()
    elif choice=='5':
        break
    else:
        print('wrong choice')
