# Factorial of 6=  6 * 5 * 4 * 3 * 2 * 1 = 720
# Using Recursive Function

def Factorial(n):
    ''' This is the program to return factorial
        of any number using recursion
    '''
    if(n==0 or n==1):
        return 1
    else:
        return n * Factorial(n-1)



number=eval(input("Enter any number: "))
fact=Factorial(number)
print(Factorial.__doc__)
print("Factorial of ", number, "is ",fact)