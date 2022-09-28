#!/usr/bin/python3
"""
Importing the modules needed
"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
args = load_from_json_file(filename)

for i in range(len(argv)):
    args.append(argv[i])

save_to_json_file(args, filename)