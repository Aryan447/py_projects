def binarySearch(myArr, target):
    start = 0
    end = len(myArr) - 1

    while(start<=end):
        mid = start + (end-start)/2
        mid = int(mid)

        if (target<myArr[mid]):
            end = mid - 1
        elif(target>myArr[mid]):
            start = mid + 1
        else:
            return mid

    return - 1
      
    

myArray = [1, 2, 11, 22, 33, 44, 55, 66, 77]
target = 11
ans = binarySearch(myArray, target)

print("item is at",ans+1,"th position")
