file = open("sale_data.csv","w")
try:
    purchase_quantity = int(input("Quantity of purchase: "))
    original_balance = int(input("Initial balance: "))
    final_balance = int(input("Final amount: "))

    profit = final_balance - original_balance
    print(profit,original_balance)
    profit_rate = (profit/original_balance) * 100
    unit = original_balance/purchase_quantity

    print(profit, profit_rate, unit,sep="-")
    print(profit, profit_rate, unit,sep=",",file="file")
except ValueError:
    print("Input values must be numbers")
except ZeroDivisionError:
    print("input values must be greater than 0")
file.close()