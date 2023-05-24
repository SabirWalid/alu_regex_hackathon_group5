#!/usr/bin/python3
import re
def check_episode_titles(episode_title):
    pattern = r"^(.*) S\d{2}E\d{2}: .*$"
    match = re.match(pattern, episode_title)
    if match:
        return True
    else:
        return False
Episode_titles = [
"Bamenya S02E20: New Families",
"Buhavu S12E32 : Evil mothers",
"Now we have new series"


]
for title in Episode_titles:
    if check_episode_titles(title):
        print(f"The episode '{title}' matches the pattern")
    else:
        print(f"The episode '{title}' doesn't have a match")