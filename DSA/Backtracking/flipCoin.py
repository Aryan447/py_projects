def flip_coins(n, path=""):
    # Base case: when we flipped all coins
    if len(path) == n:
        print(path)
        return

    # Choice 1: Head
    flip_coins(n, path + "H")

    # Choice 2: Tail
    flip_coins(n, path + "T")


flip_coins(2)
