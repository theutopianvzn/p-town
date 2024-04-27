#include <stdio.h>

void findWaitingTime(int n, int bt[], int wt[], int at[]) {
  int completed = 0, current_time = 0;
  while (completed != n) {
    int min_index = -1;
    for (int i = 0; i < n && at[i] <= current_time; i++) {
      if (min_index == -1 || bt[i] < bt[min_index]) {
        min_index = i;
      }
    }

    if (min_index != -1) {
      bt[min_index]--;
      current_time++;

      if (bt[min_index] == 0) {
        wt[min_index] = current_time - at[min_index] - bt[min_index];
        completed++;
      }
    } else {
      current_time++; // CPU is idle
    }
  }
}

void findTurnAroundTime(int n, int bt[], int wt[], int tat[], int at[]) {
  for (int i = 0; i < n; i++) {
    tat[i] = bt[i] + wt[i];
  }
}

void findAverageTime(int n, int bt[], int at[]) {
  int wt[n], tat[n], total_wt = 0, total_tat = 0;

  findWaitingTime(n, bt, wt, at);
  findTurnAroundTime(n, bt, wt, tat, at);

  printf("Process\t Arrival Time\t Burst Time\t Waiting Time\t Turn Around Time\n");
  for (int i = 0; i < n; i++) {
    total_wt += wt[i];
    total_tat += tat[i];
    printf("%d \t\t %d \t\t %d \t\t %d \t\t %d\n", i + 1, at[i], bt[i], wt[i], tat[i]);
  }

  float avg_wt = (float)total_wt / n;
  float avg_tat = (float)total_tat / n;

  printf("Average Waiting Time = %.2f\n", avg_wt);
  printf("Average Turnaround Time = %.2f\n", avg_tat);
}

int main() {
  int n;
  printf("Enter the number of processes: ");
  scanf("%d", &n);

  int bt[n], at[n];
  printf("Enter arrival times and burst times for %d processes:\n", n);
  for (int i = 0; i < n; i++) {
    printf("Process %d:\n", i + 1);
    scanf("%d %d", &at[i], &bt[i]);
  }

  findAverageTime(n, bt, at);

  return 0;
}
