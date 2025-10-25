from collections import deque

def bfs_recursive(graph, queue, visited):
    if not queue:
        return

    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        queue.extend(graph[node])  # add neighbors

    bfs_recursive(graph, queue, visited)  # recursive call

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
bfs_recursive(graph, deque([start]), set())

