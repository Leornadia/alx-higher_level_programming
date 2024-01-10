#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0

    for i in range(len(roman_string)):
        curr_value = roman_map.get(roman_string[i], 0)
        if i > 0 and curr_value > roman_map.get(roman_string[i - 1], 0):
            num += curr_value - 2 * roman_map.get(roman_string[i - 1], 0)
        else:
            num += curr_value

    return num
