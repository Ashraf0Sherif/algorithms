from collections import deque

def bfs(graph, start_node, target_node=None):
    queue = deque([start_node])
    
    visited = {start_node}
    parent = {start_node: None}
    
    while queue:
        current = queue.popleft()
        
        if target_node and current == target_node:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    if target_node:
        return None
    
    paths = {}
    for node in parent:
        path = []
        current = node
        while current:
            path.append(current)
            current = parent[current]
        paths[node] = path[::-1]
    
    return paths

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    path = bfs(graph, 'A', 'F')
    print("Path from A to F:", path)
    
    all_paths = bfs(graph, 'A')
    print("\nAll paths from A:")
    for node, path in all_paths.items():
        print(f"To {node}: {path}")