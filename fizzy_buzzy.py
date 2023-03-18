import random
print("***Welcome to Fizzy Buzz Game***")

for num in range(0,101):
    if(num%3==0 and num%5==0):
        print("FizzyBuzz")
    elif(num %3 == 0):
        print("Fizzy")
    elif(num%5 == 0):
        print("Buzz")
    else:
        print(num)

