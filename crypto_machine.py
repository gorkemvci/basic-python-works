import math
def cal_paint_cans():
    print("Welcome to Paint Cans Calculator")
    height= int(input("Please enter the Height: "))
    weight = int(input("Please enter the Weight: "))
    power = int(input("Coloring power (area) of a can of paint?"))
    area_cans = math.ceil((height* weight) / power )
    print(f"You will buy {area_cans} cans .")
def prime_num_cal():
    print("Welcome to Prime Number Checker")
    number = int(input("Please enter the your number: "))
    prime_checker = True
    for checker in range(2,number):
        if number % checker == 0 :
            prime_checker= False
    if prime_checker == True:
        print("This number is Prime Number.")
    else:
        print("This number is not Prime Number.")
#cal_paint_cans()
#prime_num_cal()
def ceaser_crypto():
 control = True
 while control is True:  
    text = input("Please enter your text: ")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text_list = list(text)
    codenot = int(input("What is your code: "))
    code = int((codenot % 26))
    choice = int(input("What do you want?\n If you want crypto please press 1 or decrypto press 2:\n") )
    if choice == 1:
        for text_index in range(len(text)):
            newlocation =  alphabet.index(text_list[text_index]) + code
            text_list[text_index] = alphabet[newlocation] 
    else:
       for text_index in range(len(text)):
        newlocation =  alphabet.index(text_list[text_index]) - code
        text_list[text_index] = alphabet[newlocation] 
    text_string = ''.join(map(str,text_list))
    print(f"Your text is {text_string} in code {codenot}\n")
    if input("Do you want a new crypto or de crypto? If you want press 1 or Dont want press 2:\n") is 2:
        print("GoodBye")
        control = False
    else:
        ceaser_crypto()   
     
ceaser_crypto()






