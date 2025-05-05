import heapq

def prim_mst(graph):
    if not graph:
        return {}
    
    start_vertex = list(graph.keys())[0]
    
    mst_vertices = {start_vertex}
    all_vertices = set(graph.keys())
    
    mst = {v: [] for v in all_vertices}
    
    edge_heap = []
    
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(edge_heap, (weight, start_vertex, neighbor))
    
    while edge_heap and len(mst_vertices) < len(all_vertices):
        weight, u, v = heapq.heappop(edge_heap)
        
        if v not in mst_vertices:
            mst_vertices.add(v)
            mst[u].append((v, weight))
            mst[v].append((u, weight))
            
            for neighbor, w in graph[v]:
                if neighbor not in mst_vertices:
                    heapq.heappush(edge_heap, (w, v, neighbor))
    
    return mst

if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('D', 1)],
        'B': [('A', 2), ('C', 3), ('D', 2)],
        'C': [('B', 3), ('D', 4)],
        'D': [('A', 1), ('B', 2), ('C', 4)]
    }
    
    mst = prim_mst(graph)
    
    print("Minimum Spanning Tree:")
    total_weight = 0
    edges = []
    
    for u in mst:
        for v, weight in mst[u]:
            if (v, u) not in edges:
                edges.append((u, v))
                total_weight += weight
                print(f"Edge: {u} - {v}, Weight: {weight}")
    
    print(f"Total MST Weight: {total_weight // 2}")