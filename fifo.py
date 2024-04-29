from queue import Queue 

def pageFaults(pages, n, capacity): 
    s = set() 
    indexes = Queue() 
    page_faults = 0
    hits = 0
    
    for i in range(n): 
        if (len(s) < capacity): 
            if (pages[i] not in s): 
                s.add(pages[i]) 
                page_faults += 1
                indexes.put(pages[i]) 
            else:
                hits += 1

        else: 
            if (pages[i] not in s): 
                val = indexes.queue[0] 
                indexes.get() 
                s.remove(val) 
                s.add(pages[i]) 
                indexes.put(pages[i]) 
                page_faults += 1
            else:
                hits += 1

    misses = page_faults
    hit_ratio = (hits / n) * 100
    miss_ratio = (misses / n) * 100

    return hits, misses, hit_ratio, miss_ratio

if __name__ == '__main__': 
    pages = [6,0,2,1,0,5,6,3,0,4,2,1,0,1,2] 
    n = len(pages) 
    capacity = 3
    hits, misses, hit_ratio, miss_ratio = pageFaults(pages, n, capacity)
    print("Number of Hits:", hits)
    print("Number of Misses:", misses)
    print("Hit Ratio:", hit_ratio, "%")
    print("Miss Ratio:", miss_ratio, "%")
