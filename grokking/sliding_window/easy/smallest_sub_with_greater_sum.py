"""
The time complexity of the above algorithm will be O(N):
    The outer for loop runs for ALL elements,
    and the inner while loop processes each element only ONCE
    therefore, the time complexity of the algorithm will be O(N+N)
    which is asymptotically equivalent to O(N)
"""


def smallest_subarray_sum(s, arr):
    window_start, window_sum, smallest_size = 0, 0.0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            # slide and shrink
            size = window_end - window_start + 1
            smallest_size = min(smallest_size, size) if smallest_size else size
            window_sum -= arr[window_start]
            window_start += 1

    return smallest_size
