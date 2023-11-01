#!/usr/bin/python3
for char_ascii in range(97, 123):
    if char_ascii != 113 and char_ascii != 101:
        print("{char_ascii:c}".format(char_ascii=char_ascii), end='')
