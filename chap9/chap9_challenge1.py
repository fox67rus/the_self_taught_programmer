import os
file_path = os.path.join("C:",
                         "Users",
                         "fox",
                         "Desktop",
                         "check-list.txt")
print(file_path)
with open(r"C:\Users\fox\Desktop", "r") as f:
    print(f.read())
