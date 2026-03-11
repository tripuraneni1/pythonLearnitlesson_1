# calc total startup cost
# project monthly revenue
# monthly operating expense
# determine monthly profit: Substract monthly operating cost from revenue
# implemente security Analysis
# format and display results
from pythonlearnit.exercises.lesson4_startup_financial_calculator import equipment_cost, basic_tier_price, \
    pro_tier_price
from pythonlearnit.exercises.lesson4_startup_financial_calculator_solution import total_startup_cost, \
    new_monthly_revenue

dev_cost = 5000
marketing_cost = 2000
equipment_cost = 10000

# subscription tiers
basic_tier_price = 9.99
pro_tier_price = 19.99
basic_tier_users = 1000
pro_tier_users = 1500

#monthly operating expense
server_cost = 1000
support_cost = 5000
misc_cost = 2000

# Calc total startup cost
total_startup_cost = dev_cost + marketing_cost + equipment_cost

# calc month revenue

monthly_revenue = (basic_tier_price * basic_tier_users) + (pro_tier_price * pro_tier_users)
# calc monthly operating cost
monthly_operating_cost = server_cost + support_cost + misc_cost
# calc monthly profit
monthly_profit = monthly_revenue - monthly_operating_cost

# montly nreak even
months_to_break_even = total_startup_cost / monthly_profit
# print
print("Financial Project")
print(f"print total startup cost: $ {total_startup_cost:,.2f}")
print(f"Monthly Revenue: ${monthly_revenue:,.2f}")
print(f"Monthly Profit: ${monthly_profit:,.2f}")
print(f"Months to Break Even: ${months_to_break_even:,.1f}")

#sensitivity anlysis
print("\n sensitivity analysis")
basic_tier_users +=500
pro_tier_users +=200
# recalc metric with new user number
new_monthly_revenue = (basic_tier_users * basic_tier_price) + (pro_tier_users * pro_tier_price)
new_monthly_profit = new_monthly_revenue - monthly_operating_cost
new_months_to_break_even = total_startup_cost / new_monthly_profit

print("Updated Financial Projects:")
print(f"New Monthly Revenue: ${new_monthly_revenue:,.2f}")
print(f"New Monthly Profit: ${new_monthly_profit:,.2f}")
print(f"New Months to Break Even: {new_months_to_break_even:,.1f}")

revenue_increase = new_monthly_revenue - monthly_revenue
profit_increase = new_monthly_profit - monthly_profit
break_even_improvemtn = months_to_break_even - new_months_to_break_even

print("/n Impact of User Increase:")
print(f"Revenue Increase ${revenue_increase:,.2f}")
print(f"Profit Increase ${profit_increase:,.2f}")
print(f"Break even improvement {break_even_improvemtn:,.2f}")
