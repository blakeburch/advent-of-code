import re
import argparse


def is_number(text):
    if text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return True
    else:
        return False


def find_written_number_matches(text):
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine))'
    matches = re.findall(pattern, text)
    return matches


def convert_text_to_number(text, written_number):
    num_lookup = {
        "one": "1e",
        "two": "2o",
        "three": "3e",
        "four": "4r",
        "five": "5e",
        "six": "6x",
        "seven": "7n",
        "eight": "8t",
        "nine": "9e",
    }
    text = text.replace(written_number, num_lookup[written_number], 1)
    return text


def read_file_contents(file_path):
    calibrations = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip newline characters and add to the list
            calibrations.append(line.strip())
    return calibrations


def convert_calibration_to_numbers(calibration):
    matches = find_written_number_matches(calibration)
    for match in matches:
        calibration = convert_text_to_number(calibration, match)
    return calibration


def create_first_and_last_value(calibration):
    working_number_list = []
    for char in calibration:
        if is_number(char):
            working_number_list.append(char)
    if len(working_number_list) == 0:
        return 0
    else:
        final_value = int(working_number_list[0] + working_number_list[-1])
    return final_value


parser = argparse.ArgumentParser(description='Process a file.')
parser.add_argument('--file', type=str, default='sample_1.txt',
                    help='The name of the file to process')
args = parser.parse_args()

calibrations = read_file_contents(args.file)

final_number_list = []
new_calibrations = []

for calibration in calibrations:
    calibration = convert_calibration_to_numbers(calibration)
    new_calibrations.append(calibration)

for calibration in new_calibrations:
    first_and_last_value = create_first_and_last_value(calibration)
    final_number_list.append(first_and_last_value)

print(sum(final_number_list))
