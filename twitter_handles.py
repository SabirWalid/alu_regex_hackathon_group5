#!/usr/bin/python3
import re

pattern = r"@[\w\d]+"

handle = input("Enter a Twitter handle: ")

if re.match(pattern, handle):
    print(f"{handle} is a valid Twitter handle")
else:
    print(f"{handle} is not a valid Twitter handle")
