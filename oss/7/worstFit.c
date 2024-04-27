#include <stdio.h>

void worstFit(int blockSize[], int m, int processSize[], int n) {
    int allocation[n];

    // Initialize allocation to -1 to indicate not allocated
    for (int i = 0; i < n; i++) {
        allocation[i] = -1;
    }

    // Pick each process and find the worst fit block for it
    for (int i = 0; i < n; i++) {
        int worstIdx = -1; // Index of worst fit block
        for (int j = 0; j < m; j++) {
            if (blockSize[j] >= processSize[i]) {
                if (worstIdx == -1 || blockSize[j] > blockSize[worstIdx]) {
                    worstIdx = j;
                }
            }
        }

        if (worstIdx != -1) {
            // Allocate block to process
            allocation[i] = worstIdx;
            blockSize[worstIdx] -= processSize[i];
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

    worstFit(blockSize, m, processSize, n);

    return 0;
}
