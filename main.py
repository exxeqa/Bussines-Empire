import os
import random
balance = 10000
stocks = {}
crypto = {}
businesses = {}

stocks_market = {
    1: ("Apple", 150),
    2: ("Tesla", 250),
    3: ("Microsoft", 400)
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def bal_check():
    print(f"Ваш баланс: ${balance}")

def stock_check():
    for key, value in stocks.items():
        print(f"Акция: {key}, количество: {value}")
    for key, value in crypto.items():
        print(f"Криптовалюта: {key}, количество: {value}")
    for key, value in businesses.items():
        print(f"Бизнес: {key}, количество: {value}")

def stock_have_check(name):
    global have_stock
    if name in stocks:
        have_stock = True
    else:
        have_stock = False
    return have_stock

def buy_stock():
    global balance, price, buy_am, name
    while True:
        try:
            buy_am = int(input("Сколько акций купить: "))
            if buy_am * price > balance:
                print("Недостаточно средств")
                continue
            else:
                balance -= buy_am * price
                print("Покупка успешна!")
                print(f"Куплено: {buy_am} {name}\nПотрачено ${buy_am * price}\nБаланс: {balance}$ ")
                if name in stocks:
                    stocks[name] += buy_am
                else:
                    stocks[name] = buy_am
                break
        except ValueError:
            print("Введите число!")
            continue

def sell_print():
    try:
        amout_s = stocks[name]
        print(f"Продано: {sell_am} {name}\nПолучено: {sell_am * price}$\nБаланс {balance}$\nОсталось акций {amout_s}")
    except KeyError:
        print(f"Продано: {sell_am} {name}\nПолучено: {sell_am * price}$\nБаланс {balance}$\nАкций не осталось")

def sell_stock():
    while True:
        global sell_am, balance
        if stock_have_check(name) == True:
            amout = stocks[name]
            while True:
                try:
                    sell_am = int(input(f"Сколько вы хотите продать акций {name}"))
                    pass
                except ValueError:
                    clear()
                    print("Enter number!")
                    continue
                if sell_am > amout:
                    print("Нельзя продать больше акций, чем есть")
                    continue
                elif sell_am < 0:
                    print("Нельзя продать отрицательное кол-во акций")
                    continue
                elif sell_am == 0:
                    print("Нельзя продать 0 акций")
                    continue
                else:
                    if amout - sell_am == 0:
                        del stocks[name]
                        balance += sell_am * price * 1.1
                        sell_print()
                        break
                    else:
                        stocks[name] = sell_am
                        balance += sell_am * price * 1.1
                        sell_print()
                        break
        else:
            print(f"Вы не владеете акциями {name}")
            break

def stock_market():
    global balance, price, buy_am, name
    x = 1
    print(f"{"=" * 24}\n{" " * 6}STOCK MARKET{" " * 6}\n{"=" * 24}\n\nБаланс: ${balance}")
    for i in range(len(stocks_market)):
        name, price = stocks_market[x]
        print(f"{x}. {name}  ${price} ")
        x += 1
    x -= 1
    while True:
        try:
            user_input = int(input(f"Выберите интересующую вас акцию 1-{x}: "))
            if user_input <= x:
                name, price = stocks_market[user_input]
                break
            else:
                print(f"Выберите акцию 1-{x}")
                continue
        except ValueError:
            print("Введите число!")
            continue
    print(f"{name} - ${price}")
    bal_check()
    while True:
        try:
            mode = int(input("Выберите режим\n1. Купить акции\n2. Продать акции\n3. Назад"))
            pass
        except ValueError:
            clear()
            print("Enter number!")
            continue
        if mode == 1:
            buy_stock()
            break
        elif mode == 2:
            sell_stock()
        elif mode == 3:
            break
        else:
            print("choose between 1 - 3")
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