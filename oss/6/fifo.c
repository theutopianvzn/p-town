#include <stdio.h>

void fifo(int page[], int n, int frames) {
    int pageFaults = 0;
    int m, s, temp[frames];

    for (m = 0; m < frames; m++) {
        temp[m] = -1;  // Initialize frame content with -1 (invalid page)
    }

    printf("\nRef String\t Page Frames\n");
    for (m = 0; m < n; m++) {
        s = 0;
        for (int j = 0; j < frames; j++) {
            if (page[m] == temp[j]) {   // Check if page is already in a frame
                s = 1;
                break;
            }
        }

        if (s == 0) {  // Page fault occurs if not found
            pageFaults++;
            for (int j = 0; j < frames - 1; j++) {  // Shift existing pages (FIFO)
                temp[j] = temp[j + 1];
            }
            temp[frames - 1] = page[m];  // Insert new page at the end
        }

        for (int j = 0; j < frames; j++) {
            if (temp[j] == -1) {
                printf("   \t\t");  // Print empty frame if applicable
            } else {
                printf("%d \t\t", temp[j]);
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

    fifo(page, n, frames);

    return 0;
}
