price = 19.99

price_float = float(price)

quantity = 5

total_cost = price_float * quantity

total_cost_int = int(total_cost)

print(f"Price: {price}, quantity {quantity}, total cost: {total_cost}, in Integer {total_cost_int}, in type {type(price_float)}, total_cost_in type: {type(total_cost_int)}")