from collections import defaultdict, deque

def pageFaults(pages, n, capacity): 
    page_faults = 0
    hits = 0
    cache = defaultdict(int)  # Dictionary to store the last accessed time of each page
    queue = deque()  # Queue to maintain the order of page accesses
    
    for page in pages:
        if page in cache:
            hits += 1
            queue.remove(page)  
        else:
            page_faults += 1
            if len(cache) == capacity:
                evicted_page = queue.popleft()
                del cache[evicted_page]
                
            cache[page] = page_faults 
        queue.append(page)  # Add the current page to the end of the queue

    misses = page_faults
    hit_ratio = (hits / n) * 100
    miss_ratio = (misses / n) * 100

    return hits, misses, hit_ratio, miss_ratio

if __name__ == '__main__': 
    pages = [7, 0, 1, 2, 0, 3, 0, 
             4, 2, 3, 0, 3, 2, 1,2,0,1,7,0,1] 
    n = len(pages) 
    capacity = 4
    hits, misses, hit_ratio, miss_ratio = pageFaults(pages, n, capacity)
    print("Number of Hits:", hits)
    print("Number of Misses:", misses)
    print("Hit Ratio:", hit_ratio, "%")
    print("Miss Ratio:", miss_ratio, "%")
