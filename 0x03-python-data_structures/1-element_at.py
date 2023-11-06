#!/usr/bin/python3

def element_at(my_list, idx):
    list_len = len(my_list)
    if (idx > list_len or idx < 0):
        return None
    i = 0
    for i in range(list_len - 1):
        if i == idx:
            return my_list[i]
