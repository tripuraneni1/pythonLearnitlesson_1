def process_number(number):
    total = sum(number)
    average = total / len(number)
    minimum = min(number)
    maximum = max(number)
    return f"Total: {total}, Average: {average}, Minimum: {minimum}, Maximum: {maximum}"

result = process_number([1,2,3,4,5])

float_result = process_number([1.3,2.5,7.3,4.8,5.9])
print(f"Integer results {result} and float result {float_result}")