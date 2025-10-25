def selectionSort(myArr):
    for i in range(len(myArr)-1):
        smallest = i
        for j in range(i+1, len(myArr)):
            if myArr[smallest]>myArr[j]:
                smallest = j

        myArr[smallest], myArr[i] = myArr[i], myArr[smallest]
    return myArr


myArray = [7, 8, 3, 1, 2]

print(selectionSort(myArray))
