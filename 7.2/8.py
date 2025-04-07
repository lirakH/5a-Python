a = input("Numri pjestues \n")

try:
    z = 12 / int(a)
except Exception as e:
    print( "errori i cili shfaqet eshte", e)
finally:
    print("finally executed")



print("kodi ne fund")



def calculate(number1, number2, operator):
    """Performs the given arithmetic operation on two numbers."""
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    else:
        raise ValueError("Invalid operation")

result = calculate(5,2,"-")
print(result)
