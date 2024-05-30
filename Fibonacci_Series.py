# Fibonacci Series Program:
# f0,f1 = 0 , 1
# f2 = f0 + f1
# fn= f(n-1) + f(n-2)
# 0 1 1 2 3 5 ...............
def FibonacciOf(n):
     s1, s2, count= 0, 1, 0
     if(n<=0):
         print("Please enter positive number..")
     elif(n==1):
         print(s1)
     else:
         while (count<n):
             print(s1, end=" ")
             sn=s1+s2
             s1=s2
             s2=sn
             count+=1



length=eval(input("Enter the length of fibonacci series : "))
FibonacciOf(length)