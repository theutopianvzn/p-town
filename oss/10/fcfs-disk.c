#include <stdio.h>
#include <math.h>

void FCFS(int request[], int n, int head) {
    int seek_count = 0;
    printf("Head starts at %d\n", head);

    for (int i = 0; i < n; i++) {
        seek_count += abs(request[i] - head);
        head = request[i];
        printf("Seek cost for request %d: %d\n", i + 1, abs(request[i] - head));
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

    FCFS(request, n, head);

    return 0;
}
