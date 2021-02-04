# Write a Python program to convert an integer to a roman numeral.
# Roman digits are: digits = ["M", "CM", "D", "CD”, "C", "XC", "L", "XL”, "X", "IX", "V", "IV", "I"]
import math
import sys
def int_to_roman(number: int) -> str:
    # roman number range is 1 - 3,999
    # check if number out of range of roman number
    if( number < 1 or number > 3999):
        return "Input out of range of roman numberal"
    roman_number = ""
    # declare dictionary to map arabic number to roman
    roman_dict = { 
        1000: "M",
        900 : "CM",
        500 : "D",
        400 : "CD",
        100 : "C",
        90  : "XC",
        50  : "L",
        40  : "XL",
        10  : "X",
        9   : "IX",
        5   : "V",
        4   : "IV",
        1   : "I",
        0   : ""
    }
    number_of_digits =  len(str(number))
    for i in range(number_of_digits)[::-1]:
        place_value = 10**i             # i.e. 1000, 100, 10, 1
        digit = number // place_value   # get digit
        #digit 1 - 3
        if(digit >= 1 and digit <= 3):
            roman_number += (roman_dict[1 * place_value] * digit)
        #digit 6 - 8
        elif(digit >= 6 and digit <= 8):
            roman_number += roman_dict[5 * place_value] + (roman_dict[1 * place_value] * (digit-5))
        #digit 0, 4, 5, 9
        else:
            roman_number += roman_dict[digit*place_value]
        number = number % place_value
    return roman_number

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python int_to_roman.py <number between 1 - 3,999>")
        exit()
    print(int_to_roman(sys.argv[1]))
