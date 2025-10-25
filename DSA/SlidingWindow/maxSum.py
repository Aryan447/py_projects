def maxSum(arr, k):
    n = len(arr)
    if n < k:
        return None

    windowSum = sum(arr[:k])
    max_sum = windowSum

    for i in range(n-k):
        windowSum = windowSum - arr[i] + arr[i+k]
        max_sum = max(max_sum, windowSum)

    return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 3
result = maxSum(arr, k)
print(result)  # Output: 21 (from [1, 0, 20])
