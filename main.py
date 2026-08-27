import os
import random

balance = 10000
stocks = {}
crypto = {}
businesses = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bal_check():
    print(f"Ваш баланс: ${balance}")

def stock_check():
    print(f"Акции {stocks}\nКриптовалюта {crypto}\nБизнесы {businesses}")

def menu():
    global mode
    print(f"{"=" * 24}\n{" " * 5}BUSINESS EMPIRE{" " * 5}\n{"=" * 24}\n\nБаланс: ${balance}")
    print("1. Просмотреть баланс")
    print("2. Просмотреть активы")
    print("3. Выход")

    while True:
        try:
            mode = int(input("Enter choice: "))
            return mode
        except ValueError:
            clear()
            print("Enter number!")
            continue

run = True

while run:
    mode = menu()
    if mode == 1:
        clear()
        bal_check()
    elif mode == 2:
        clear()
        stock_check()
    elif mode == 3:
        break
    else:
        print("choose between 1 - 3")
        continue