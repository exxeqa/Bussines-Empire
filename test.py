stocks_market = {
    "Apple": 150,
    "Tesla": 250,
    "Microsoft": 400
}
x = 1
for key, value in stocks_market.items():
    print(f"{x}. {key}  ${value} ")
    x += 1
