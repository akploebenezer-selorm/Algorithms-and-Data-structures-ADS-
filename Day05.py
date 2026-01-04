"""
Merging Intervals

Algorithm:
1. Sort intervals by start time
2. Add first interval to merged list
3. Loop through remaining intervals
4. Merge overlapping intervals
5. Return merged list
"""

def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: sort intervals by start
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


# Example test
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
