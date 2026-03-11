# Cel to Farenheight converter with extra examples
#This script converts temp from C to F
#Author
#Date
#Revision

days_in_week = 7
celsius_temp = 25.0
pi = 3.14159 #Example of float constanct
greeting = "Hello, "
user_name = "Python Learner"

is_summer = True
month = ["Jan", "Feb", "Mar"]
temp_scales = {"Celsius" : "C", "Farenheit" : "F"}
celcius_to_farenheit_Factor = 9/5
farenheit_offset = 32
farenheit_temp = (celsius_temp * celcius_to_farenheit_Factor) + farenheit_offset
farenheit_temp = round(farenheit_temp,1)

full_greeting = greeting + user_name
shouted_greeting = full_greeting.upper()
whispered_greeting = full_greeting.lower()
month_count = len(month)
output1 = str(celsius_temp) + temp_scales["Celsius"] + "is equal to " + str(farenheit_temp) + temp_scales["Farenheit"]

output2 = f"{celsius_temp}{temp_scales["Celsius"]} is equal to {farenheit_temp}{temp_scales["Farenheit"]}"

print(full_greeting)
print(shouted_greeting)
print(whispered_greeting)
print(f"Number of month is: {month_count}")
print(output1)
print(output2)
print(f"Is this summer?: {is_summer}")
print(f"there are {days_in_week} days in week and pi is approximately {pi:.2f}%")