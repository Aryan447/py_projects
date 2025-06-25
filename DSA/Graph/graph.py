vertexData = ['A', 'B', 'C', 'D']

adjacencyMatrix = [
    [0, 1, 1, 1], # Edges for A
    [1, 0, 1, 0], # Edges for B
    [1, 1, 0, 0], # Edges for C
    [1, 0, 0, 0]  # Edges for D
]

def print_adjacencyMatrix(matrix):
    for row in matrix:
        print(row)

def print_connections(matrix, vertices):
    print("\nconnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:  # if there is a connection
                print(vertices[j], end=" ")
        print()  # new line

print(vertexData)
print_adjacencyMatrix(adjacencyMatrix)
print_connections(adjacencyMatrix, vertexData)
