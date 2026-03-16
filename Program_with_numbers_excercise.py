# # weekly_groceries = float(input("Enter weekly groceries spending$: "))
# # weekly_groceries = weekly_groceries * 4
# # print(f"montly groceries: {weekly_groceries}")
#
# celcius = float(input("Enter Celcius: "))
# fahrenheit = celcius * 1.8 + 32
# print(f"tempareture in fahrenheit: {fahrenheit}")
#
# bill_amount = float(input("Enter bill: "))
# tip_percent = float(input("Enter tip percent: "))
# tip = bill_amount * tip_percent/100
# print(f"{bill_amount} is that bill amount {tip_percent} tip percent, so that total tip is {tip}")

# savings_goal = int(input("Enter savings goal: "))
# monthly_savings = int(input("Enter monthly savings: "))
# months_to_goal = savings_goal / monthly_savings
# print(f"months to reach goal: {months_to_goal}")
# wall_area = int(input("Enter wall area: "))
# paint_coverage = int(input("Enter paint coverage: "))
# paint_needed = wall_area / paint_coverage
# print(f"paint needed{paint_needed:,.2f}%")

import math
# wall_area = float(input("Enter wall area: "))
# paint_area = float(input("Enter paint area: "))
# paint_needed = wall_area / paint_area
# ceil_round = math.ceil(paint_needed)
# floor_round = math.floor(paint_needed)
# normal_round = round(paint_needed)
#
# round_to_half = round(paint_needed *2)/2
# print(f" Exact amount {paint_needed:,.2f}")
# print(f" Rounded Up {ceil_round:,.2f}")
# print(f" Round Down {floor_round:,.2f}")
# print(f" Normal {normal_round:,.2f}")
# print(f" Round to half {round_to_half:,.2f}")

# weigth = float(input("Enter weigth: "))
# height = float(input("Enter height: "))
# BMI = weigth / (height **2)
# print(f"BMI: {BMI}")



# principal = float(input("Enter principal: "))
# interest_rate = float(input("Enter interest rate: "))
# loan_term = float(input("Enter load term : "))
# Mortgate_payment = principal * (interest_rate * (1 + interest_rate) ** loan_term) / (((1 + interest_rate) ** loan_term - 1))
# print (f"Mortgate_payment {Mortgate_payment}")
def time_to_float(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60
def float_to_time(time_float):
    hours = int(time_float)
    minutes = int((time_float - hours) * 60)
    return f"{hours:02d}:{minutes:02d}"
local_time_str = input("Enter local time in (24 time format, HH:MM: ")
LocalTime = time_to_float(local_time_str)
time_difference = float(input("Enter time difference (+ for ahead and - for behind"))
converted_time = (LocalTime + time_difference) % 24
converted_time_str = float_to_time(converted_time)
print (f"The converted time is {converted_time_str}")

