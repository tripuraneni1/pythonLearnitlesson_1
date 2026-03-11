from pythonlearnit.exercises.lesson3_split_the_bill_solution import individual_share, total_with_tip

total_bill = int(input("Enter the total bill: "))
number_of_friend = 5
individual_share = total_bill / number_of_friend

print(f"Total bill: {total_bill} and each friend should pay {individual_share}")

tip_percent = 0.15
tip_amount = tip_percent * total_bill
total_with_tip = tip_amount + total_bill

rounded_sum = round(total_with_tip, 2)
print(f"Original amount: {total_bill}")
print(f"total amount: {total_with_tip}\n rounded sum: {rounded_sum}")