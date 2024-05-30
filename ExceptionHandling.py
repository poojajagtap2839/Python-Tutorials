# finally block is always executed
def func():
    try:
        num = int(input("enter number : "))
        for i in range(1, num):
            print(i)
            if i==4:
                break
        else:
            print("done")

    except:
       print("please enter integer number.")

    finally:
         print("Im always Executed")


func()












