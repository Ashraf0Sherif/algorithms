def activity_selection(start, finish):
    n = len(start)
    selected = [0]
    
    for i in range(1, n):
        if start[i] >= finish[selected[-1]]:
            selected.append(i)
    
    return selected

if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    selected_activities = activity_selection(start, finish)
    print("Selected activities:", selected_activities)