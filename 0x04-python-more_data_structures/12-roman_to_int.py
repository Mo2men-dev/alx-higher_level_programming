#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    lst = []
    i = 0
    while i < len(roman_string):
        crr_n = roman_dic[roman_string[i]] 
        if i != len(roman_string) - 1:
            if crr_n < roman_dic[roman_string[i + 1]]:
                lst.append(roman_dic[roman_string[i + 1]] - crr_n)
                i += 1
            else:
                lst.append(crr_n)
        else:
            lst.append(crr_n)
        i += 1
    return sum(lst)

print(roman_to_int("III"))      # Output: 3
print(roman_to_int("IX"))        # Output: 9
print(roman_to_int("LVIII"))     # Output: 58
print(roman_to_int("CDXLIV"))    # Output: 444
print(roman_to_int("CMXCIX"))    # Output: 999
print(roman_to_int("MMMCMXCIX")) # Output: 3999

