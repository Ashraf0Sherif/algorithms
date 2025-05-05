def dfs(graph, start_node, target_node=None):
    visited = set()
    path = []
    found = [False]
    
    def dfs_recursive(node):
        if found[0]:
            return
            
        visited.add(node)
        path.append(node)
        
        if target_node and node == target_node:
            found[0] = True
            return
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
                if found[0]:
                    return
                    
                if target_node and not found[0]:
                    path.pop()
    
    dfs_recursive(start_node)
    
    if target_node:
        return path if found[0] else None
    return path

def dfs_iterative(graph, start_node, target_node=None):
    stack = [start_node]
    visited = set()
    parent = {start_node: None}
    
    while stack:
        current = stack.pop()
        
        if current in visited:
            continue
            
        visited.add(current)
        
        if target_node and current == target_node:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        
        neighbors = graph.get(current, [])
        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                parent[neighbor] = current
                stack.append(neighbor)
    
    if target_node:
        return None
    
    return list(visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    path = dfs(graph, 'A', 'F')
    print("Path from A to F (recursive):", path)
    
    path_iterative = dfs_iterative(graph, 'A', 'F')
    print("Path from A to F (iterative):", path_iterative)
    
    traversal = dfs(graph, 'A')
    print("\nDFS traversal from A:", traversal)