import numpy as np
import pandas as pd

ticker = []
quantity = []
with open("data/portfolio.txt", encoding='utf8') as file:
    lines = file.readlines()
    for line in lines:
        stock = line.split()
        ticker.append(stock[0])
        quantity.append(stock[1])
portfolio = pd.DataFrame({"ticker": ticker, "quantity": quantity})
portfolio.to_csv('data/portfolio.csv', index=False)
