def fcfs_schedule():
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for process {i}: "))
        burst_time = int(input(f"Enter burst time for process {i}: "))
        processes.append((i, arrival_time, burst_time))

    processes.sort(key=lambda x: x[1])  # Sort processes based on arrival time
    current_time = 0
    waiting_time_total = 0
    turnaround_time_total = 0
    
    print("Process ID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
    
    for process in processes:
        process_id, arrival_time, burst_time = process
        
        completion_time = max(current_time, arrival_time) + burst_time

        waiting_time =  completion_time - arrival_time - burst_time

        turnaround_time = completion_time - arrival_time

        waiting_time_total += waiting_time
        turnaround_time_total += turnaround_time

        print(f"{process_id}\t\t{arrival_time}\t\t{burst_time}\t\t{completion_time}\t\t{waiting_time}\t\t{turnaround_time}")
        
        # Update current time
        current_time = completion_time

    avg_waiting_time = waiting_time_total / num_processes
    avg_turnaround_time = turnaround_time_total / num_processes
    
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

if __name__ == "__main__":
    fcfs_schedule()


