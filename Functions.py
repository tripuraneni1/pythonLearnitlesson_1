from pythonlearnit.exercises.lesson3_Savings_Caclulater_solution import rounded_average

print("Hellow, World")
print()
print("Bye", "Then")


number = "123"
print(f"Number length {len(number)}")

number = "1234"
integer = int(number)
float_number = float(number)

integer = 3
float_number = 5.4
print(integer + float_number)

my_sum = integer + float_number
print (round(my_sum,2))

print (min(integer,float_number))
print (max(integer,float_number))

number = [1,2,3,4,5]
average = sum(number)/len(number)
print(f"The average is: {average}")
rounded_average = round(average,2)
print(f"The rounded average is {rounded_average}")
mixed_list = [1, "two", 3.0, 4.0]

for item in mixed_list:
    print(f" the type of {item} is {type(item)} ")


message = "hello, world !"
print(message.upper())
words = message.split(", ")
print(words)

print(",".join(words.capitalize() for words in words   ))

fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))
print(" - ".join(fruits))

word = "Python"
print(", ".join(reversed(word)))