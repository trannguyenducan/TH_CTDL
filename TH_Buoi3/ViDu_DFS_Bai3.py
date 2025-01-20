def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex) # Them cac nut ke vao ngan xep (dao nguoc de duyet theo thu tu)
            neighbors = reversed(graph[vertex])
            stack.extend(neighbors)
            print(f"Da day cac nut ke cua '{vertex}' vao ngan xep: {list(neighbors)}")
    print()

# Minh hoa
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS tu nut A:")
dfs(graph, 'A') # A C F B E D      