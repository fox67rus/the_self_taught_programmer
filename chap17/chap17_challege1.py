import re
text = ""
with open("zen.txt", "r") as f:
    text = f.read()

matches = re.findall("голландец", text, re.IGNORECASE)
print(matches)