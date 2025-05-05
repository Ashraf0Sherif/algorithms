def activity_selection(start, finish):
    # Pair each activity's start and finish time with its original index
    activities = list(enumerate(zip(start, finish)))
    
    # Sort activities by finish time
    activities.sort(key=lambda x: x[1][1])
    
    selected = []
    last_finish_time = 0

    for index, (s, f) in activities:
        if s >= last_finish_time:
            selected.append(index)
            last_finish_time = f

    return selected

if __name__ == "__main__":
    start = [4, 0, 1, 1, 3]
    finish = [6, 2, 3, 6, 4]
    selected_activities = activity_selection(start, finish)
    print("Selected activities:", selected_activities)
