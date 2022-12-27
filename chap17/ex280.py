import re
t = "__один__ __два__ __три__"
found = re.findall("__.*?__", t)

for match in found:
    print(match)
