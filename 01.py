#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
our_password= [] 
print("*****Welcome to the PyPassword Generator!*****")
nr_letters=  int(input("How many letters would you like in your password?\n"))  
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
for let in range(0,nr_letters):
    our_password.append(random.choice(letters))
for sym in range(0,nr_symbols):
    our_password.append(random.choice(symbols))
for num in range(0,nr_numbers):
    our_password.append(random.choice(numbers))
random.shuffle(our_password)
our_password = "".join(our_password) #list to stirng with .join
print("Your Password = " + our_password)
