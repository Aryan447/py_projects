def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    dp = [0] * (num+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, num + 1):
        dp[i] = dp[i-2] + dp[i-1]

    return dp


print(fib(3))
