import re
line = "123?34 привет?"

m = re.findall("\d", line, re.IGNORECASE)

print(m)