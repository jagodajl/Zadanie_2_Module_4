import logging

logging.basicConfig(level=logging.INFO)


def addition(x, y):
    logging.info("1.Dodawanie: " + str(x) + " + " + str(y))
    return x + y


def subtraction(x, y):
    logging.info("2.Odejmowanie: " + str(x) + " - " + str(y))
    return x - y


def multiplication(x, y):
    logging.info("3.Mnożenie: " + str(x) + " * " + str(y))
    return x * y


def division(x, y):
    logging.info("4.Dzielenie: " + str(x) + " / " + str(y))
    return x / y


def is_action_input_valid(action_input):
    casted_action_input = int(action_input)
    if casted_action_input >= 1 and casted_action_input <= 4:
        return True
    else:
        logging.error("The action input must be in range of 1 - 4. Please provide correct action input")
        return False


def is_number_input_valid(number1, number2):
    if number1.isnumeric() and number2.isnumeric:
        return True
    else:
        logging.error("One of provided component is not a number. Please run again providing only numbers")
        exit(0)


user_input = input("Podaj działanie, posługując się odpowiednią liczbą: (1 - dodawanie  2 - odejmowanie  3 - mnozenie "
                   " 4 - dzielenie) :) ")


def perform_calculation(user_input):
    while is_action_input_valid(user_input):
        number1_str = input("Podaj składnik 1: ")
        number2_str = input("Podaj składnik 2 ")
        is_number_input_valid(number1_str, number2_str)
        num1 = float(number1_str)
        num2 = float(number2_str)

        if user_input == '1':
            print("Wynik to:  ", addition(num1, num2))

        elif user_input == '2':
            print("Wynik to:  ", subtraction(num1, num2))

        elif user_input == '3':
            print("Wynik to:  ", multiplication(num1, num2))

        elif user_input == '4':
            print("Wynik to:  ", division(num1, num2))
        break


perform_calculation(user_input)
