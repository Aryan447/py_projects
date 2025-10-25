def rollDice(n, path=""):
    if len(path) == n:
        print(path)
        return 1  # 1 possibility found

    count = 0

    for face in "123456":
        count += rollDice(n, path + face)  # add possibilities from deeper calls

    return count


total = rollDice(2)
print("All possibilities =", total)
