#!/usr/bin/python3
import re

pattern = r'^\[Verse\d+\].*$'

song = input("Enter a song lyrics in the format '[Verse X] some lyrics': ")

match = re.match(pattern, song)

if match:
  print("This is a match")
  else:
    print("This isnt a match")
