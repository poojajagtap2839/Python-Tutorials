# Secret Code
# Coding : If the word contains atleast 3 characters, remove first letter and append it at the end.
# now append random 3 characters at the starting and at the end
# else:
#       simply reverse the string.


user_input= input("Enter any message : ")
num=int(input("Enter 1 to code the message and enter 2 to decode the message: "))
seperated_str= user_input.split()
newstr = []

match(num):
    case 1:
        for word in seperated_str:

            if(len(word)>3):
                start="wer"
                end= "mnj"
                str= start + word[1:]+ word[0]+ end
                newstr.append(str)

            else:
                 reverse= word[: :-1]
                 newstr.append(reverse)

        print(" ".join(newstr))

    case 2:
        for word in seperated_str:
            if(len(word) >3):
                str= word[-4]+ word[3:-4]
                newstr.append(str)

            else:
                reverse= word[: :-1]
                newstr.append(reverse)
        print(" ".join(newstr))




