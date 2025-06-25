def palindroneNumber(x):
    if x < 0:
        return False
    reverse = 0
    xcopy = x
    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x //= 10

    return reverse == xcopy

x = 363

print(palindroneNumber(x))