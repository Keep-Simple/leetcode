"""
In many problems dealing with an array (or a LinkedList),
we are asked to find or calculate something
among all the subarrays/sublists of a given size.

For example, take a look at this problem:
Given an array, find the average
of all subarrays of ‘K’ contiguous elements in it.

 Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
 Here, we are asked to find the average
 of all subarrays of ‘5’ contiguous elements in the given array
"""


# brute-force
# time = O(N*K), for each n we calculate its next K elements
def find_averages_of_subarrays(K, arr):
    result = []
    for i in range(len(arr) - K + 1):
        # find sum of next 'K' elements
        _sum = 0.0
        for j in range(i, i + K):
            _sum += arr[j]
        result.append(_sum / K)  # calculate average

    return result


# time = O(N), iterating only once
def find_averages_of_subarrays_sliding_window(K, arr):
    result = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide
        # if we've not hit the required window size of 'k'
        if window_end >= K - 1:
            result.append(window_sum / K)  # calculate the average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    result_sliding = find_averages_of_subarrays_sliding_window(
        5, [1, 3, 2, 6, -1, 4, 1, 8, 2]
    )
    print("Averages of subarrays of size K: " + str(result))
    print("*Sliding: Averages of subarrays of size K: " + str(result_sliding))


main()
