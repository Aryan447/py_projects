def mySqrt(num):
    if(num == 0 or num == 1):
        return num
    
    start = 1
    end = num

    while(start<=end):
        mid = start + (end - start) // 2
        square = mid * mid
        if(square == num):
            return mid
        elif(square < num):
            start = mid + 1
        else:
            end = mid - 1
        
    return end



myNum = 9
print(mySqrt(myNum))