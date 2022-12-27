import re

line = "Красивое лучше, чем уродливое."

matches = re.findall("красивое", line, re.IGNORECASE)
print(matches)


