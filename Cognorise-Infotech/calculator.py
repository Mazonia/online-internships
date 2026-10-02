
def add(num1=1, num2=1):
    sumx = num1 + num2
    print(sumx)


def sub(num1=1, num2=1):
    subt = num1 - num2
    print(subt)


def div(num1=1, num2=1):
    divi = num1 / num2
    print(divi)


def mult(num1=1, num2=1):
    multi = num1 * num2
    print(multi)


def exp(num1, num2):
    expo = num1 ** num2
    print(expo)


def mod(num1, num2):
    modu = num1%num2
    print(modu)


while True:

    print("Welcome to the SIMPLE CALCULATOR")
    print("What would you like to use the calculator for?")
    print(" 1. ADD\n", "2. SUBTRACT\n", "3. DIVIDE\n", "4. MULTIPLY\n", "5. MODULOS\n", "6. EXPONENT\n", "7. QUIT\n")
    try:
        x = input("Enter the number option")
        if x == "7" or x.upper() == "QUIT":
            break

        number1 = int(input("Enter your first number"))
        number2 = int(input("Enter your second number"))

        if x == "1" or x.upper() == "ADD":
            add(number1, number2)

        elif x == "2" or x.upper() == "SUBTRACT":
            sub(number1, number2)

        elif x == "3" or x.upper() == "DIVIDE":
            try:
                div(number1, number2)
            except ZeroDivisionError:
                print("This is a Zero Division Error")

        elif x == "4" or x.upper() == "MULTIPLY":
            mult(number1, number2)

        elif x == "5" or x.upper() == "MODULOS":
            mod(number1, number2)

        elif x == "6" or x.upper() == "EXPONENT":
            exp(number1, number2)

        else:
            print("Come again later")

    except ValueError:
        print("Start over and Enter a number")


