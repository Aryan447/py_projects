def missingNumber(arr):
    n = len(arr)
    # The expected sum from 0 to n
    expected_sum = (n * (n + 1)) // 2
    # Actual sum of array
    actual_sum = sum(arr)
    # The missing number is the difference
    return expected_sum - actual_sum

myArray = [3, 0, 1];
print(missingNumber(myArray))
