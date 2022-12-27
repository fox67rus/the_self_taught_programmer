import re
string = " Два даа."

m = re.findall("д[ав]а", string, re.IGNORECASE)

print(m)