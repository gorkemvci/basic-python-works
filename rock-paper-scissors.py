import random


print("******Day04 Project******")
print("****Rock-Paper-Scissors****")
print("Welcome to This Game")
print('''Rules:
Rock: 0
Paper:1
Scissors:2
End Game:5
''')
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''   

while(True):
    computer_choice = random.randint(0,2)
    gamer_choice=int(input("Please press 0-1-2 or 5(End GAME)\n"))
    if(gamer_choice == 5):
        break
    else:
        if(computer_choice==0 and gamer_choice ==2 or computer_choice==2 and gamer_choice==1):
            print("Computer is WIN :(")
        elif(computer_choice==1 and gamer_choice==0):
            print("Computer is WIN :(")
        elif(computer_choice==gamer_choice):
            print("Equal :/ We dont have a Winner :/")
        elif(gamer_choice>2):
            print("Invalid Number")
        else:
            print("Wooww.. You are Winner :)")



