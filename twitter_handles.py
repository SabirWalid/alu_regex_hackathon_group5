import re

pattern = r"@[\w\d]+"

handle1 = "@shema123"
handle2 = "@joe_foe"
handle3 = "@aluEducation"

if re.match(pattern, handle1):
    print(f"{handle1} is a valid Twitter handle")
else:
    print(f"{handle1} is not a valid Twitter handle")

if re.match(pattern, handle2):
    print(f"{handle2} is a valid Twitter handle")
else:
    print(f"{handle2} is not a valid Twitter handle")

if re.match(pattern, handle3):
    print(f"{handle3} is a valid Twitter handle")
else:
    print(f"{handle3} is not a valid Twitter handle")