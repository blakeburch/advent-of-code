import unittest
from part_two import is_number, find_written_number_matches, convert_text_to_number, convert_calibration_to_numbers, create_first_and_last_value


class TestIsNumber(unittest.TestCase):

    def test_valid_numbers(self):
        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            self.assertTrue(is_number(num))

    def test_invalid_numbers(self):
        for text in ['a', '10', '', 'one']:
            self.assertFalse(is_number(text))


class TestFindWrittenNumberMatches(unittest.TestCase):

    def test_valid_matches(self):
        self.assertEqual(find_written_number_matches(
            "I have two apples and three oranges"), ['two', 'three'])
        self.assertEqual(find_written_number_matches(
            "one four nine"), ['one', 'four', 'nine'])
        self.assertEqual(find_written_number_matches(
            "eightwothree"), ['eight', 'two', 'three'])
        self.assertEqual(find_written_number_matches(
            "sqrdkpzeight936oneighth"), ['eight', 'one', 'eight'])
        self.assertEqual(find_written_number_matches(
            "ftwonevbhlhlqhsix5dzfqgsone"), ['two', 'one', 'six', 'one'])

    def test_no_matches(self):
        self.assertEqual(find_written_number_matches(
            "eleven twelve thirteen"), [])


class TestConvertTextToNumber(unittest.TestCase):

    def test_valid_conversions(self):
        self.assertEqual(convert_text_to_number(
            "I have one apple", "one"), "I have 1 apple")
        self.assertEqual(convert_text_to_number(
            "eightwothree", "eight"), "8wothree")
        self.assertEqual(convert_text_to_number(
            "8wothree", "three"), "8wo3")


class TestConvertCalibrationToNumbers(unittest.TestCase):

    def test_convert_with_written_numbers(self):
        self.assertEqual(convert_calibration_to_numbers(
            "I have two apples and three oranges"), "I have 2 apples and 3 oranges")
        self.assertEqual(convert_calibration_to_numbers(
            "eightwothree"), "8wo3")

    def test_convert_without_written_numbers(self):
        self.assertEqual(convert_calibration_to_numbers(
            "I have apples and oranges"), "I have apples and oranges")


class TestCreateFirstAndLastValue(unittest.TestCase):

    def test_valid_calibration(self):
        self.assertEqual(create_first_and_last_value(
            "12345"), 15)
        self.assertEqual(create_first_and_last_value(
            "1234d"), 14)
        self.assertEqual(create_first_and_last_value(
            "a234d"), 24)

    def test_no_numbers(self):
        # Assumes default to 0 if no numbers
        self.assertEqual(create_first_and_last_value("abcde"), 0)

    def test_single_number(self):
        self.assertEqual(create_first_and_last_value("a1bcd"),
                         11)  # Assumes single number repeated


if __name__ == '__main__':
    unittest.main(verbosity=2)
