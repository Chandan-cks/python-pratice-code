n=int(input("Enter a number: "))
f1=0
f2=1
print("Fevonassi series-")
print(f1,end=" ")
print(f2,end=" ")
fn=f1+f2
while(fn<=n):
    print(fn,end=" ")
    f1=f2
    f2=fn
    fn=f1+f2

print(fn,end=" ")
