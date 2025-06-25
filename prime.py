import math
import time

start = time.time()
def isPrime(n):
    if n<2: return False

    for i in range(2, int(math.sqrt(n))+1):
        if (n%i == 0): return False
    return True


print(isPrime(100))
print(f"time took {time.time() - start:.2f} seconds")