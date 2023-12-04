from operator import truediv


def is_number(text):
    if text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return True
    else:
        return False


def read_file_contents(file_path):
    calibrations = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip newline characters and add to the list
            calibrations.append(line.strip())
    return calibrations


calibrations = read_file_contents('input.txt')

working_number_list = []
final_number_list = []

for calibration in calibrations:
    for char in calibration:
        if is_number(char):
            working_number_list.append(char)
    final_value = int(working_number_list[0] + working_number_list[-1])
    final_number_list.append(final_value)
    working_number_list = []

print(sum(final_number_list))
