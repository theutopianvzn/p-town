#include <stdio.h>

void firstFit(int blockSize[], int m, int processSize[], int n) {
    int allocation[n];

    // Initialize allocation to -1 to indicate not allocated
    for (int i = 0; i < n; i++) {
        allocation[i] = -1;
    }

    // Pick each process and find the first fit block for it
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (blockSize[j] >= processSize[i]) {
                // Allocate block to process
                allocation[i] = j;
                blockSize[j] -= processSize[i];
                break; // Once a fit is found, break out of the inner loop
            }
        }
    }

    printf("\nProcess No\t Process Size\t Block No\n");
    for (int i = 0; i < n; i++) {
        if (allocation[i] != -1) {
            printf("%d \t\t %d \t\t %d\n", i + 1, processSize[i], allocation[i] + 1);
        } else {
            printf("%d \t\t %d \t\t Not Allocated\n", i + 1, processSize[i]);
        }
    }
}

int main() {
    int m, n;
    printf("Enter the number of blocks: ");
    scanf("%d", &m);
    printf("Enter the block sizes:\n");
    int blockSize[m];
    for (int i = 0; i < m; i++) {
        scanf("%d", &blockSize[i]);
    }

    printf("Enter the number of processes: ");
    scanf("%d", &n);
    printf("Enter the process sizes:\n");
    int processSize[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &processSize[i]);
    }

    firstFit(blockSize, m, processSize, n);

    return 0;
}
