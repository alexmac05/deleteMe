from random import randint

def myfunction():
    x = 1 + 1
    x = x + 10
    return x

def play():
    random_int = randint(0,100)

    while True:
        user_guess = int(input("What number did we guess (0-100)?"))

        if user_guess == random_int:
            print(f"You found the number ({random_int}). Congrats!")
            break

        if user_guess < random_int:
            print("Your number is less than the number we guessed.")
            continue

        if user_guess > random_int:
            print("Your number is more than the number we guessed,")
            continue

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #play()
    print("hello world")
    ok = myfunction()
    print(ok)

    print("OK does this hit?")
    sally = myfunction()
    print(sally)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



