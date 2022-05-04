#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count = 0

    for i in range(len(roman_string)):
        if i < (len(roman_string)) - 1 and letter[roman_string[i]] < letter[roman_string[i + 1]]:
            count -= letter[roman_string[i]]
        else:
            count += letter[roman_string[i]]

    return count
