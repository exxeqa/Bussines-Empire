import os
import random
balance = 10000
stocks = {}
crypto = {}
businesses = {}

stocks_market = {
    "Apple": 150,
    "Tesla": 250,
    "Microsoft": 400
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bal_check():
    print(f"Ваш баланс: ${balance}")

def stock_check():
    print(f"Акции {stocks}\nКриптовалюта {crypto}\nБизнесы {businesses}")

def stock_market():
    x = 1
    print(f"{"=" * 24}\n{" " * 6}STOCK MARKET{" " * 6}\n{"=" * 24}\n\nБаланс: ${balance}")
    for key, value in stocks_market.items():
        print(f"{x}. {key}  ${value} ")
        x += 1
    x -= 1
    while True:
        try:
            choose = int(input(f"Выберите акцию 1-{x}: "))
            if choose > x:
                print(f"Please choose between 1-{x}")
                continue
            else:
                break
        except ValueError:
            print("Enter number!")
            continue

def menu():
    global mode
    print(f"{"=" * 24}\n{" " * 5}BUSINESS EMPIRE{" " * 5}\n{"=" * 24}\n\nБаланс: ${balance}")
    print("1. Просмотреть баланс")
    print("2. Просмотреть активы")
    print("3. Фондовый рынок")
    print("4. Выход")

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
        clear()
        stock_market()
    elif mode == 4:
        break
    else:
        print("choose between 1 - 4")
        continue