class Trebuchet:
    @staticmethod
    def get_digits_in_single_line(line):
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        return digits

    @staticmethod
    def solution():
        total = 0
        with open('./sample/aoc_day1') as sample_input:
            lines = sample_input.readlines()
            for line in lines:
                digits_in_line = Trebuchet.get_digits_in_single_line(line)
                line_value_pairs = f'{digits_in_line[0]}{digits_in_line[len(digits_in_line) - 1]}'
                total += int(line_value_pairs)
        return total
