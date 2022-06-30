def max_sub_array_of_size_k(k, arr):
    window_start, window_sum, max_sum = 0, 0.0, 0.0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k:
            # slide
            window_sum -= arr[window_start]
            max_sum = max(max_sum, window_sum)
            window_start += 1

    return max_sum
