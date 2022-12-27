import re
text = "Приведение прошуршало и исчезло в углу."

match1 = re.findall(".ло", text, re.IGNORECASE)
print(match1)

match2 = re.findall("[аз]ло", text, re.IGNORECASE)
print(match2)