#Case 1: 股票价格数据处理（TXT+列表）
from numpy.ma.core import append
from numpy.ma.extras import average

close_price = 0
total_price = 0
stock=[]
filtered_stocks=[]
with open ("../stock_prices.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
                parts = line.split()
                name = parts[0]
                price = int(parts[1])
                stock.append([name,price])
                total_price += price
        close_price = total_price/4
        print(f"平均收盘价：{close_price}")
        for stock,price in stock:
                if price > 500:
                        filtered_stocks=[stock,price]
with open ("filtered_stocks.txt", "w", encoding="utf-8") as file:
        lines = file.writelines()