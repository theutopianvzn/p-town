#include <stdio.h>

#define MAX_PROCESS 10
#define MAX_RESOURCE 5

void isSafe(int processes, int available[], int max[][MAX_RESOURCE], int allocation[][MAX_RESOURCE], int need[][MAX_RESOURCE]) {
    int work[MAX_RESOURCE];
    for (int i = 0; i < MAX_RESOURCE; i++) {
        work[i] = available[i];
    }

    int finish[MAX_PROCESS] = {0};
    int count = 0;

    while (count < processes) {
        int found = 0;
        for (int i = 0; i < processes; i++) {
            if (finish[i] == 0) {
                int canFinish = 1;
                for (int j = 0; j < MAX_RESOURCE; j++) {
                    if (need[i][j] > work[j]) {
                        canFinish = 0;
                        break;
                    }
                }

                if (canFinish) {
                    for (int j = 0; j < MAX_RESOURCE; j++) {
                        work[j] += allocation[i][j];
                    }
                    finish[i] = 1;
                    count++;
                }
                found = 1;
            }
        }

        if (found == 0) {
            printf("System is in an unsafe state\n");
            return;
        }
    }

    printf("System is in a safe state\n");
}

int main() {
    int processes, resources;
    printf("Enter the number of processes: ");
    scanf("%d", &processes);
    printf("Enter the number of resources: ");
    scanf("%d", &resources);

    int available[MAX_RESOURCE];
    printf("Enter available resources:\n");
    for (int i = 0; i < resources; i++) {
        scanf("%d", &available[i]);
    }

    int max[MAX_PROCESS][MAX_RESOURCE];
    printf("Enter maximum resource needs for each process:\n");
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < resources; j++) {
            scanf("%d", &max[i][j]);
        }
    }

    int allocation[MAX_PROCESS][MAX_RESOURCE];
    printf("Enter allocated resources for each process:\n");
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < resources; j++) {
            scanf("%d", &allocation[i][j]);
        }
    }

    int need[MAX_PROCESS][MAX_RESOURCE];
    for (int i = 0; i < processes; i++) {
        for (int j = 0; j < resources; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    isSafe(processes, available, max, allocation, need);

    return 0;
}
