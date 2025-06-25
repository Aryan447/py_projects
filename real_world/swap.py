num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

print("Before Swap: ", num1, num2)

num2 = num2 - num1
num1 = num2 + num1
num2 = num1 - num2
print("After Swap", num1, num2)