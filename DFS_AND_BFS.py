def DFS(graph, start, end):
    stack = [(start, [start])]  
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == end:
            return path  
        if node not in visited:
            visited.add(node)

            for neighbor in reversed(graph.get(node, [])):  
                stack.append((neighbor, path + [neighbor]))
                print((neighbor, path + [neighbor]))

    return None




def BFS(graph, start,end):
    queue = [(start, [start])]  
    visited = set()

    while queue:
        node, path = queue.pop(0)

        if node == end:
            return path  
        if node not in visited:
            visited.add(node)

            for neighbor in reversed(graph.get(node, [])):  
                queue.append((neighbor, path + [neighbor]))
                print((neighbor, path + [neighbor]))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
end = 'F'

print(BFS(graph, start, end))