def fib(n):
    if n==0: return 0
    if n==1: return 1
    return fib(n-1) + fib(n-2)

num = 7
for i in range(num+1):
    print(fib(i), end=" ")
