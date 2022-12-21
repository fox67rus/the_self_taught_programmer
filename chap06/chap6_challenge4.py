s = "Где это? Кто это? Когда это?"
s = s.split("?")
s.pop()
s2 = []

for i in s:
    s2.append(i.strip() + "?")
print(s2)

# решение автора, но оно не верное
lst = "Где это? Кто это? Когда это?".split("?")
print(lst)
