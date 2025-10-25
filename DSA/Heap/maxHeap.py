'''
in this we will implement max heap using soom trick as the max heap is not available in the python by default
the min heap returns the min element of the error i.e the array[0] will have the smallest element
the max heap returns the max element of the error i.e the array[0] will have the largest element
we will negate the array first then we will create the heap then we will negate the elements again
'''

import heapq

arr = [3, 6, 9]

negarr = [-x for x in arr]

heapq.heapify(negarr)

print(negarr)

posarr = [-x for x in negarr]
print(posarr) # [ 9, 6, 3]

stone = -heapq.heappop(negarr)

print(stone) # this will return 9


