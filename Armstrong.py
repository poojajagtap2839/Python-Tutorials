# Program to check whether entered number is armstrong number or not
# 153 = 1^3+ 5^3 + 3^3 = 1 + 125 + 27 =153
def Armstrong(num):
    sum = 0
    index=0
    num1=num
    while(num1>0):
        rem = num1%10
        num1= num1//10
        index += 1
    print("Total no of digits: ", index)

    while(num>0):
        rem = num%10
        sum = sum+(rem ** index)
        num = num//10

    return sum



number=eval(input("Enter any number: "))
result=Armstrong(number)
if(number==result):
    print(number , "is an Armstrong Number")
else:
    print(number , "is not an Armstrong Number")