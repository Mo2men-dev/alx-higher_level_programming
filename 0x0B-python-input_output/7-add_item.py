#!/usr/bin/python3
"""load add and save module"""
import os
import sys


save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

list_o = []

if os.path.exists("add_item.json"):
    list_o = load_from("add_item.json")

for i in range(1, len(sys.argv)):
    list_o.append(sys.argv[i])

save_to(list_o, "add_item.json")
