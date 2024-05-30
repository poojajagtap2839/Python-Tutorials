# Koun Banega Crorepati ???


questions =[
    ["Who is the Prime Minister of India?", "Narendra Modi", "Uddhav Takrey","Manmohan Singh","APJ Abdul Kalam", 1],
    ["Who is the father of nation?","Lala Lajapatray","shasatri Ji","Gandhi Ji","Nehru Ji", 3],
    ["Which country comes first in the population?", "India", "China", "Rassia", "America", 2],
    ["Which gas human needs for breathing?","NO2" ,"O2","H2","SO2",2],
    ["Who is the Prime Minister of India?", "Narendra Modi", "Uddhav Takrey", "Manmohan Singh", "APJ Abdul Kalam", 1],
    ["Who is the father of nation?", "Lala Lajapatray", "shasatri Ji", "Gandhi Ji", "Nehru Ji", 3],
    ["Which country comes first in the population?", "India", "China", "Rassia", "America", 2],
    ["Which gas human needs for breathing?", "NO2", "O2", "H2", "SO2", 2],
    ["Who is the Prime Minister of India?", "Narendra Modi", "Uddhav Takrey", "Manmohan Singh", "APJ Abdul Kalam", 1],
    ["Who is the father of nation?", "Lala Lajapatray", "shasatri Ji", "Gandhi Ji", "Nehru Ji", 3],
    ["Which country comes first in the population?", "India", "China", "Rassia", "America", 2],
    ["Which gas human needs for breathing?", "NO2", "O2", "H2", "SO2", 2],
    ["Who is the Prime Minister of India?", "Narendra Modi", "Uddhav Takrey", "Manmohan Singh", "APJ Abdul Kalam", 1],
    ["Who is the father of nation?", "Lala Lajapatray", "shasatri Ji", "Gandhi Ji", "Nehru Ji", 3],
    ["Which country comes first in the population?", "India", "China", "Rassia", "America", 2],

]

amounts=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
price=0
print("Let's begin the game ....\nKoun Banega Crorepati ???\n")

for i in range(0,len(questions)):
    question=questions[i]
    if (i == 4):
        price = 10000
    elif (i == 9):
        price = 320000
    elif (i == 14):
        price = 10000000

    print(f"Your question for RS. {amounts[i]}: {question[0]} " )
    print(f" A] {question[1]}      B] {question[2]} ")
    print(f" C] {question[3]}      D] {question[4]} ")

    reply=int(input("Enter your reply in (1-4) or 0 to quit the game: "))

    if(reply ==question[-1]):

        print(f"Congrats!! you won RS.{amounts[i]}\n\n")

    elif (reply == 0):

         price=amounts[i-1]
         print(f"You have quited your game here...................\nYour take home money is RS.{price}")
         break
    else:
        print("Sorry, You choose wrong answer")
        print(f"Your take home money is RS.{price}")
        break






else:
    print("Now, You have become Crorepati 🙌🙌")






