def insertionSort(unsortArray):
    for i in range(1, len(unsortArray)):
        key = unsortArray[i]
        j = i - 1
        while (j >= 0) and unsortArray[j] > key:
            unsortArray[j + 1] = unsortArray[j]
            j = j - 1
        unsortArray[j + 1] = key
    return unsortArray


myArray = [5, 4, 3, 2, 1]
print(insertionSort(myArray))
