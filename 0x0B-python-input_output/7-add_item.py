#!/usr/bin/python3

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    prev_content = load_from_json_file(filename)
except FileNotFoundError:
    prev_content = []

save_to_json_file(prev_content + argv[1:], filename)
