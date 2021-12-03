i=0
str1='Hello World'
print("length of %s is %d"%(str1,len(str1)))
while i < len(str1):
    if str1[i] == 'w':
        i +=1
        break
    print('Current Letter :', str1[i])
    i += 1
   
    
