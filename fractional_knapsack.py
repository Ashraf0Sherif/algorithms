def fractional_knapsack(values, weights, capacity):
    items = [(v/w, v, w, i) for i, (v, w) in enumerate(zip(values, weights))]
    
    items.sort(reverse=True)
    
    total_value = 0
    taken = [0] * len(values)
    
    remaining_capacity = capacity
    
    for ratio, value, weight, index in items:
        if remaining_capacity >= weight:
            taken[index] = 1.0
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            taken[index] = fraction
            total_value += value * fraction
            break
    
    return total_value, taken

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    
    max_value, items_taken = fractional_knapsack(values, weights, capacity)
    
    print("Maximum value:", max_value)
    print("Items taken (fraction):")
    for i, fraction in enumerate(items_taken):
        if fraction > 0:
            print(f"Item {i}: Value = {values[i]}, Weight = {weights[i]}, Fraction = {fraction}")
            
    total_weight = sum(weights[i] * fraction for i, fraction in enumerate(items_taken))
    print(f"Total weight: {total_weight}/{capacity}")