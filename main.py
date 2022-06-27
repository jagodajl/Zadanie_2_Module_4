import logging
logging.basicConfig(level=logging.DEBUG)

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


while True:
    choice = input("Podaj działanie, posługując się odpowiednią liczbą: (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj składnik 1: "))
        num2 = float(input("Podaj składnik 2 "))

        if choice == '1':
            print("Wynik to:  ", addition(num1, num2))

        elif choice == '2':
            print("Wynik to:  ", subtraction(num1, num2))

        elif choice == '3':
            print("Wynik to:  ", multiplication(num1, num2))

        elif choice == '4':
            print("Wynik to:  ", division(num1, num2))
        break
    else:
        print("Invalid Input")


logging.info("Podaj działanie, posługując się odpowiednią liczbą:")
logging.info("1.Dodawanie")
logging.info("2.Odejmowanie")
logging.info("3.Mnożenie")
logging.info("4.Dzielenie")