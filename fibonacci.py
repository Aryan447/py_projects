def fib(n):
    a = 0
    b = 1
    
    print(a)
    if (n == 1): return
    print("", b)
    for i in range(2, n):
        next = a + b
        print("", next)
        a = b
        b = next

num = 5
fib(num)
