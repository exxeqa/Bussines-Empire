stocks_market = {
    "Apple": 150, "1": 1,
    "Tesla": 250, "2": 2,
    "Microsoft": 400, "3": 3
}
x = 1
for key, value in stocks_market.items():
    print(f"{x}. {key}  ${value} ")
    x += 1
x = str(x)
print(stocks_market[x])