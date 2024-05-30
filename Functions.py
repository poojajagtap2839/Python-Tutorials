def sum(*numbers):
    s=0
    for num in numbers:
        s=s+num
    print("Sum of all numbers: ", s)

def average(*numbers):
    s1=0
    for num in numbers:
        s1=s1+num
    avg=s1/len(numbers)
    print("Average of all numbers: ", avg)


s=sum(5,6)
average(1,2,3,4,5,6,7)