#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_l = len(my_list) - 1
    if (idx > list_l or idx < 0):
        return my_list

    my_list[idx] = element
    return my_list
