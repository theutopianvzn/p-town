#include <stdio.h>

void findWaitingTime(int n, int bt[], int wt[], int quantum) {
    int rem_bt[n];  // Stores remaining burst time for each process
    for (int i = 0; i < n; i++) {
        rem_bt[i] = bt[i];
    }

    int t = 0; // Current time
    int completed = 0;
    while (completed != n) {
        for (int i = 0; i < n; i++) {
            if (rem_bt[i] > 0) {
                if (rem_bt[i] > quantum) {
                    rem_bt[i] -= quantum;
                    t += quantum;
                } else {
                    t += rem_bt[i];
                    wt[i] = t - bt[i];
                    rem_bt[i] = 0;
                    completed++;
                }
            }
        }
    }
}

void findTurnAroundTime(int n, int bt[], int wt[], int tat[]) {
    for (int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
    }
}

void findAverageTime(int n, int bt[], int quantum) {
    int wt[n], tat[n], total_wt = 0, total_tat = 0;

    findWaitingTime(n, bt, wt, quantum);
    findTurnAroundTime(n, bt, wt, tat);

    printf("Process\t Burst Time\t Waiting Time\t Turn Around Time\n");
    for (int i = 0; i < n; i++) {
        total_wt += wt[i];
        total_tat += tat[i];
        printf("%d \t\t %d \t\t %d \t\t %d\n", i + 1, bt[i], wt[i], tat[i]);
    }

    float avg_wt = (float)total_wt / (float)n;
    float avg_tat = (float)total_tat / (float)n;
    printf("Average Waiting Time = %.2f\n", avg_wt);
    printf("Average Turnaround Time = %.2f\n", avg_tat);
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    int bt[n];
    printf("Enter process burst time:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &bt[i]);
    }

    int quantum;
    printf("Enter the time quantum: ");
    scanf("%d", &quantum);

    findAverageTime(n, bt, quantum);
    return 0;
}
