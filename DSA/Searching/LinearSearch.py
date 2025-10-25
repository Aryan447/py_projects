def linearSearch(myarr, target):
    # Convert the input set to a list for linear search

    if len(myarr) == 0:
        return -1

    for index in range(len(myarr)):
        element = myarr[index]
        if element == target:
            return index

    return -1

# Example usage
myArray = [1, 2, 12, 44, 51, 5, 119, 92, 25]
target = 25
ans = linearSearch(myArray, target)

print("item is at",ans+1,"th position") 