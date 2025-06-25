def addDigits(num):
    while num > 9:
        temp = num % 10
        num //= 10
        num = num + temp
    return num


myNum = 38
print(addDigits(myNum))