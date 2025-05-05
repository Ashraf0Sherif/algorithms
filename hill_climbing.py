import random
import math

def hill_climbing(objective_function, start_state, get_neighbors, max_iterations=1000):
    current_state = start_state
    current_value = objective_function(current_state)
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current_state)
        
        best_neighbor = None
        best_value = current_value
        
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            if neighbor_value > best_value:
                best_neighbor = neighbor
                best_value = neighbor_value
        
        if best_neighbor is None:
            break
            
        current_state = best_neighbor
        current_value = best_value
    
    return current_state, current_value

if __name__ == "__main__":
    def objective_function(point):
        x, y = point
        return -(x**2 + y**2) + 5
    
    def get_neighbors(point):
        x, y = point
        step_size = 0.1
        neighbors = [
            (x + step_size, y),
            (x - step_size, y),
            (x, y + step_size),
            (x, y - step_size)
        ]
        return neighbors
    
    start_point = (random.uniform(-5, 5), random.uniform(-5, 5))
    
    best_point, best_value = hill_climbing(
        objective_function,
        start_point,
        get_neighbors
    )
    
    print(f"Starting point: {start_point}")
    print(f"Best point found: {best_point}")
    print(f"Best value: {best_value}")