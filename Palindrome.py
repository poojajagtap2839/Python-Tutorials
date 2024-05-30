# Palindrome Program:

def isPalindrome(n):
     count=len(n)
    # print("No of digits: ", count)
     reverse=n[: :-1]
     print("Reverse of ",n, "is ", reverse)
     if(n==reverse):
         print(n , "is Palindrome Number.")
     else:
         print(n, "is not Palindrome Number.")


number=input("Enter any number: ")
isPalindrome(number)