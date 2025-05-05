import heapq

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def astar(graph, start, goal, heuristic):
    open_set = [(0, start)]
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    came_from = {}
    closed_set = set()

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path, g_score[current]

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor, weight in graph[current]:
            tentative_g = g_score[current] + weight
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, float('inf')

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2), ('E', 5)],
        'C': [('A', 4), ('F', 3)],
        'D': [('B', 2)],
        'E': [('B', 5), ('F', 1)],
        'F': [('C', 3), ('E', 1)]
    }

    def heuristic(n, goal):
        h = {
            'A': 7,
            'B': 6,
            'C': 2,
            'D': 1,
            'E': 0,
            'F': 1
        }
        return h[n]

    path, cost = astar(graph, 'A', 'E', heuristic)
    print("Path:", path)
    print("Cost:", cost)
