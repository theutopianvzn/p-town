def SSTF(arr, head):
    seek_sequence = []
    seek_count = 0
    tracks = arr.copy()  # Create a copy of the original list to avoid modifying it
    current_track = head

    while tracks:
        # Find the track closest to the current track
        closest_track = min(tracks, key=lambda x: abs(x - current_track))
        
        seek_time = abs(closest_track - current_track)
        seek_count += seek_time

        current_track = closest_track
        seek_sequence.append(current_track)
        tracks.remove(current_track)

    print("Seek Sequence is:", seek_sequence)
    print("Total number of track movements =", seek_count)


if __name__ == '__main__':
    arr = [82, 170, 43, 140, 24, 16, 190]
    head = 50

    SSTF(arr, head)
