
a= eval(input("enter first number: "))
b= eval(input("enter second number: "))

print(a, "is greater than",b) if a>b else print(a, "is equal to ",b) if a==b else print(b, "is greater than",a)



# Enumerate function:

list1 = [0,1,2,3,4,5]
print("................Enumerate Function..........")
for index,element in enumerate(list1):
    print(element)
    if(index==3):
        print("Hello!!")