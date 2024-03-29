

stock_prices = {"info": [600,630,620], "ril": [1430, 1490,1567], "mtl":[234,180,160]}

def avg_list(l):
    '''
    returns average of a list of numbers
    '''
    sum = 0
    for item in l:
        sum = sum + item
    average = round(float(sum / len(l)), 2) 
    return average


action = input("What action to take: ")
if action == "print":
    for key in stock_prices:
        print(key, stock_prices[key], "==> avg: ", avg_list(stock_prices[key]))
elif action == "add":
    stock = input("Enter stock ticker: ")
    if stock in stock_prices:
        price = input("Enter price of stock")
        stock_prices[stock].append(price)
    else:
        price = int(input("Enter price of stock:"))
        stock_prices[stock] = [price]
        for key in stock_prices:
            print(key, stock_prices[key], "==> avg: ", avg_list(stock_prices[key]))
        




       