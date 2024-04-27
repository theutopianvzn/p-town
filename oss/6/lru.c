#include <stdio.h>

void lru(int page[], int n, int frames) {
    int pageFaults = 0, used[frames];
    int clock_hand = 0;  // Clock hand for tracking least recently used page

    for (int i = 0; i < frames; i++) {
        used[i] = -1;  // Initialize used array with -1 (unused)
    }

    printf("\nRef String\t Page Frames\n");
    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < frames; j++) {
            if (page[i] == used[j]) {   // Check if page is already in a frame
                found = 1;
                used[j] = clock_hand;  // Update used time for the found page
                clock_hand++;           // Increment clock hand (recently used)
                break;
            }
        }

        if (!found) {  // Page fault occurs if not found
            pageFaults++;
            int leastUsedIndex = 0;

            // Find least recently used page using clock hand
            while (true) {
                if (used[leastUsedIndex] == -1) {  // Empty frame, replace it
                    break;
                } else if (used[leastUsedIndex] <= clock_hand) {
                    // If found page is older than current clock hand, replace
                    break;
                } else {
                    // Move clock hand (simulate aging)
                    used[leastUsedIndex] = -1;  // Reset used time for skipped page
                    clock_hand++;
                }
                leastUsedIndex = (leastUsedIndex + 1) % frames;  // Circular clock
            }

            used[leastUsedIndex] = i;  // Insert new page at the least recently used index
            clock_hand++;               // Increment clock hand after replacement
        }

        for (int j = 0; j < frames; j++) {
            if (used[j] == -1) {
                printf("   \t\t");  // Print empty frame if applicable
            } else {
                printf("%d \t\t", page[used[j]]);
            }
        }
        printf("\n");
    }

    printf("\nPage Faults = %d\n", pageFaults);
}

int main() {
    int page[], n, frames;

    printf("Enter number of pages: ");
    scanf("%d", &n);

    printf("Enter reference string: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &page[i]);
    }

    printf("Enter number of frames: ");
    scanf("%d", &frames);

    lru(page, n, frames);

    return 0;
}
