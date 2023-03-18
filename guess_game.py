import random as r
print("***Guess A Number***")
guess_num = r.randint(1,10)
game_engine = True
heart = 5
while game_engine == True:
    if heart == 0 :
        print("Bay bay Stupid")
        game_engine = False
    guess = int(input("What is your Guess?(1-10) "))
    if guess == guess_num:
        print(f"Your guess is Correct. Your guess is {guess_num}")
    else:
        heart = heart - 1
        print(f"Your guess is not Correct. Your guess is {guess}")
        print(f"Your heart {heart}")