def FCFS(arr, head):
    seek_count = 0
    distance, cur_track = 0, 0

    for track in arr:
        distance = abs(track - head)
        seek_count += distance
        head = track
        
    print("Seek Sequence is:")
    for track in arr:
        print(track)
        
    print("Total number of track movements =", seek_count)
    

if __name__ == '__main__':
    arr = [82, 170, 43, 140, 24, 16, 190]
    head = 50

    FCFS(arr, head)
