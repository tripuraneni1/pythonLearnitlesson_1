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