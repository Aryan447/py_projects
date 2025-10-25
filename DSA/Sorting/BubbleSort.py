def bubsort(myArr):
    pass_count = 0
    for i in range(0, len(myArr)):
        pass_count += 1
        for j in range(1, len(myArr)):
            if myArr[j] < myArr[j - 1]:
                temp = myArr[j]
                myArr[j] = myArr[j - 1]
                myArr[j - 1] = temp
    return myArr, pass_count


myArray = [9, 11, 2, 4, 1]
sorted_array, total_passes = bubsort(myArray)
print(f"Sorted array: {sorted_array}")
print(f"Total passes: {total_passes}")

