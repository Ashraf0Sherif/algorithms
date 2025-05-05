def job_sequencing(jobs, deadlines):
    sorted_jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    
    max_deadline = max(deadlines)
    slot = [-1] * (max_deadline + 1)
    
    for profit, job_id in sorted_jobs:
        deadline = deadlines[job_id]
        
        for i in range(deadline, 0, -1):
            if slot[i] == -1:
                slot[i] = job_id
                break
    
    result = [job for job in slot if job != -1]
    return result

if __name__ == "__main__":
    jobs = [(100, 0), (19, 1), (27, 2), (25, 3), (15, 4)]
    deadlines = [2, 1, 2, 1, 3]
    
    sequence = job_sequencing(jobs, deadlines)
    print("Optimal job sequence:", sequence)