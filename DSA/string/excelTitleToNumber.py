order = "AB"
result = 0
for char in order:
    result = result * 26 + (ord(char) - 64)
print(result)
print(ord("A") - 64)
