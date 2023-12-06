def find_calibration_value(line):
    start = None
    final = None

    for char in line:
        if char.isdigit():
            start = int(char)
            break

    for char in reversed(line):
        if char.isdigit():
            final = int(char)
            break

    if start is not None and final is not None:
        return start * 10 + final
    else:
        return 0

def sum_calibration_values(file_name):
    total_sum = 0
    with open(file_name, 'r') as file:
        for line in file:
            total_sum += find_calibration_value(line)
    return total_sum

file_name = 'day1/example.txt'

total_calibration_sum = sum_calibration_values(file_name)
print(total_calibration_sum)
