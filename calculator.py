import arts 
print(arts.logocalculator)
def calculator():
    num1 = float(input("Please enter number-1-:\n"))
    num2 = float(input("Please enter number-2-:\n"))
    symbo = str(input("Please enter a symbol:"))
    calc={
       "+": (num1 + num2),
       "-": (num1 - num2),
       "*": (num1 * num2),
       "/": (num1 / num2)
    }
    for symbol_res in calc:
        if symbo is symbol_res:
            result= f"Result is {num1} {symbol_res} {num2} = {calc[symbol_res]}"
    print(result)
    if input("Do you want new calculate ?  yes  or no:\n") == "yes":
        calculator()
    else:
        print("GoodBye!")

calculator()