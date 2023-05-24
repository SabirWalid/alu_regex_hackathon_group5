#:/usr/bin/python3
import re

input_string = "Movie: Calvary (2014)"
pattern = re.compile('^([a-zA-Z(0-9)\s]+([0+9]{4}$))')

if pattern:
    title,year = pattern [0]

    print("Movie title:", title)
    print("Year:", year)
else:
    print("Error try again")
