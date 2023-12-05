class CalibrationProcessor:
    def __init__(self, file_name):
        self.file_name = file_name

    def find_calibration_value(self, line):
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

    def sum_calibration_values(self):
        total_sum = 0
        with open(self.file_name, 'r') as file:
            for line in file:
                total_sum += self.find_calibration_value(line)
        return total_sum

file_name = 'day1/example.txt'

calibration_processor = CalibrationProcessor(file_name)
total_calibration_sum = calibration_processor.sum_calibration_values()
print("A soma total dos valores de calibração é:", total_calibration_sum)