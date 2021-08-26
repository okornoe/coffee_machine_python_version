

# State of the coffee machine
AMOUNT_OF_WATER = 400
AMOUNT_OF_MILK = 540
AMOUNT_OF_COFFEE_BEANS = 120
AMOUNT_OF_DISPOSABLE_CUPS = 9
COFFEE_MACHINE_INCOME = 550


def check_coffee_resources_and_act(user_input):
    global AMOUNT_OF_WATER
    global AMOUNT_OF_COFFEE_BEANS
    global COFFEE_MACHINE_INCOME
    global AMOUNT_OF_MILK
    global AMOUNT_OF_DISPOSABLE_CUPS

    if user_input == 1:
        if AMOUNT_OF_WATER < 250:
            print("Sorry, not enough water!")
        elif AMOUNT_OF_COFFEE_BEANS < 16:
            print("Sorry, not enough coffee beans!")
        elif AMOUNT_OF_DISPOSABLE_CUPS < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            AMOUNT_OF_WATER = AMOUNT_OF_WATER - 250
            AMOUNT_OF_COFFEE_BEANS = AMOUNT_OF_COFFEE_BEANS - 16
            COFFEE_MACHINE_INCOME = COFFEE_MACHINE_INCOME + 4
            AMOUNT_OF_DISPOSABLE_CUPS -= 1

    elif user_input == 2:
        if AMOUNT_OF_WATER < 350:
            print("Sorry, not enough water!")
        elif AMOUNT_OF_COFFEE_BEANS < 20:
            print("Sorry, not enough coffee beans!")
        elif AMOUNT_OF_MILK < 75:
            print("Sorry, not enough milk!")
        elif AMOUNT_OF_DISPOSABLE_CUPS < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            AMOUNT_OF_WATER = AMOUNT_OF_WATER - 350
            AMOUNT_OF_MILK = AMOUNT_OF_MILK - 75
            AMOUNT_OF_COFFEE_BEANS = AMOUNT_OF_COFFEE_BEANS - 20
            COFFEE_MACHINE_INCOME = COFFEE_MACHINE_INCOME + 7
            AMOUNT_OF_DISPOSABLE_CUPS -= 1

    elif user_input == 3:
        if AMOUNT_OF_WATER < 200:
            print("Sorry, not enough water!")
        elif AMOUNT_OF_COFFEE_BEANS < 12:
            print("Sorry, not enough coffee beans!")
        elif AMOUNT_OF_MILK < 100:
            print("Sorry, not enough milk!")
        elif AMOUNT_OF_DISPOSABLE_CUPS < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            AMOUNT_OF_WATER = AMOUNT_OF_WATER - 200
            AMOUNT_OF_MILK = AMOUNT_OF_MILK - 100
            AMOUNT_OF_COFFEE_BEANS = AMOUNT_OF_COFFEE_BEANS - 12
            COFFEE_MACHINE_INCOME = COFFEE_MACHINE_INCOME + 6
            AMOUNT_OF_DISPOSABLE_CUPS -= 1


def state_of_coffee_machine():
    print("The coffee machine has:")
    print(f"{AMOUNT_OF_WATER} of water")
    print(f"{AMOUNT_OF_MILK} of milk")
    print(f"{AMOUNT_OF_COFFEE_BEANS} of coffee beans")
    print(f"{AMOUNT_OF_DISPOSABLE_CUPS} of disposable cups")
    print(f"{COFFEE_MACHINE_INCOME} of money")


def coffee_machine_buy():
    global AMOUNT_OF_WATER
    global AMOUNT_OF_COFFEE_BEANS
    global COFFEE_MACHINE_INCOME
    global AMOUNT_OF_MILK
    global AMOUNT_OF_DISPOSABLE_CUPS
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - capppuccino, back - to main:")
    user_input = input()

    if user_input == "1":
        check_coffee_resources_and_act(1)

    elif user_input == "2":
        check_coffee_resources_and_act(2)

    elif user_input == "3":
        check_coffee_resources_and_act(3)

    elif user_input == "back":
        coffee_machine_operation(input("Write action (buy, fill, take, remaining, exit):"))
        exit(0)


def coffee_machine_fill():
    print("Write how many ml of water you want to add:")
    add_water = int(input())
    global AMOUNT_OF_WATER
    AMOUNT_OF_WATER = AMOUNT_OF_WATER + add_water

    print("Write how many ml of milk you want to add:")
    add_milk = int(input())
    global AMOUNT_OF_MILK
    AMOUNT_OF_MILK += add_milk

    print("Write how many grams of coffee beans you want to add:")
    add_coffee_beans = int(input())
    global AMOUNT_OF_COFFEE_BEANS
    AMOUNT_OF_COFFEE_BEANS += add_coffee_beans

    print("Write how many disposable coffee cups you want to add:")
    add_disposable_cups = int(input())
    global AMOUNT_OF_DISPOSABLE_CUPS
    AMOUNT_OF_DISPOSABLE_CUPS += add_disposable_cups


def coffee_machine_take():
    global COFFEE_MACHINE_INCOME
    print(f"I gave you ${COFFEE_MACHINE_INCOME}")
    COFFEE_MACHINE_INCOME = 0


def coffee_machine_operation(user_input):
    if user_input == "exit":
        exit(0)
    else:
        while user_input == "buy" or user_input == "fill" or user_input == "take" or user_input == "remaining":
            if user_input == "buy":
                coffee_machine_buy()
                print()
                user_input = input("Write action (buy, fill, take, remaining, exit):")

            elif user_input == "fill":
                coffee_machine_fill()
                print()
                user_input = input("Write action (buy, fill, take, remaining, exit):")

            elif user_input == "take":
                coffee_machine_take()
                print()
                user_input = input("Write action (buy, fill, take, remaining, exit):")

            elif user_input == "remaining":
                state_of_coffee_machine()
                print()
                user_input = input("Write action (buy, fill, take, remaining, exit):")

            elif user_input == "exit":
                break


coffee_machine_operation(input("Write action (buy, fill, take, remaining, exit):"))
print()


#if __name__ == "__main__":
#    coffee_machine()

