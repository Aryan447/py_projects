import heapq

li = [5, 7, 8, 9, 11]

heapq.heapify(li)

print("The created heap is : ",end="")
print(list(li))

heapq.heappush(li,12)

# printing modified heap
print("The modified heap after push is : ")
print(list(li))

# using heappop() to pop smallest element
print("The popped and smallest element is : ")
print(heapq.heappop(li))

