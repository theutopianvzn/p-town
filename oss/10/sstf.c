#include <stdio.h>
#include <math.h>

void SSTF(int request[], int n, int head) {
    int seek_count = 0, min, min_index;

    // Create a copy of the request array to avoid modifying the original
    int copy_request[n];
    for (int i = 0; i < n; i++) {
        copy_request[i] = request[i];
    }

    printf("Head starts at %d\n", head);

    for (int i = 0; i < n - 1; i++) {
        min = abs(copy_request[0] - head);
        min_index = 0;
        for (int j = 1; j < n; j++) {
            if (abs(copy_request[j] - head) < min && copy_request[j] != -1) {
                min = abs(copy_request[j] - head);
                min_index = j;
            }
        }

        seek_count += min;
        head = copy_request[min_index];
        copy_request[min_index] = -1;  // Mark processed request

        printf("Seek cost for request %d: %d\n", min_index + 1, min);
    }

    printf("Total seek cost: %d\n", seek_count);
}

int main() {
    int n;
    printf("Enter the number of requests: ");
    scanf("%d", &n);

    int request[n];
    printf("Enter the request sequence: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &request[i]);
    }

    int head;
    printf("Enter the initial head position: ");
    scanf("%d", &head);

    SSTF(request, n, head);

    return 0;
}
