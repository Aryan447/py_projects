#matrix = [[1,2,3,4],
#          [5,6,7,8],
#         [9,10,11,12]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[2][1]) # it will print 5
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiral = []
for col in range(0, len(matrix[0])):
    spiral.append(matrix[0][col])
for row in range(1, len(matrix)):
    spiral.append(matrix[row][-1])
for col in range(len(matrix[0])-2, -1, -1):
    spiral.append(matrix[-1][col])
for col in range(0, len(matrix[1])-1):
    spiral.append(matrix[1][col])

print(spiral)
