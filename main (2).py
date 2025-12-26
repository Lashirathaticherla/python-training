# pyramid triangle pattern

x =int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end=" ")
    for j in range (i+1):
        print("*",end=" ")
    print()    
    
# hallow square pattern
n=int(input())
for i in range (n):
       for j in range(n):
           if i==0 or j==0 or i==n-1 or j==n-1:
               print("*",end=" ")
           else:
                print(" ",end=" ")
                
       print()  
       
# hallow right angled tringled pattern
n =int(input())
for i in range(n):
    for j in range(i+1):
      if i==n-1 or j==0 or i==j:
        print("*",end=" ")
      else:
        print("",end=" ")
    print()    