def generate_binary(n, path=""):
    # Base case: when path length is n
    if len(path) == n:
        print(path)
        return

    # Choice 1: Add '0'
    generate_binary(n, path + "0")

    # Choice 2: Add '1'
    generate_binary(n, path + "1")


# Try with length 3
generate_binary(3)
