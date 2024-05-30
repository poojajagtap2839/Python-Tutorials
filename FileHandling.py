
import os


os.mkdir("D:\\Python\\DemoTextFiles")
f=open("D:\\Python\\DemoTextFiles\\Text.txt" , "w")
f.write('''This is the first line.
This is second line.''')
f.close()
f=open("D:\\Python\\DemoTextFiles\\Text.txt" , "r")
print(f.readline())
print(f.readline())
f.close()
# ------------------------To check file is exist or not-------------------------------

# if os.path.exists("D:\\Python\\DemoTextFiles\\Text.txt"):
#     os.remove("D:\\Python\\DemoTextFiles\\Text.txt")
# else:
#     print("File doesnt exist......")


#  ----------------To delete the empty folder-------------------------------------

# os.rmdir("D:\\Python\\DemoTextFiles")
