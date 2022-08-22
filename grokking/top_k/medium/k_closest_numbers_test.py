import heapq

import pytest


def find_closest_elements(arr, K, X):
    """
    Given a sorted number array and two integers ‘K’ and ‘X’,
    find ‘K’ closest numbers to ‘X’ in the array.
    Return the numbers in the sorted order.
    ‘X’ is not necessarily present in the array.
    """
    # can also use two pointers
    # by starting 2 pointers from closest_idx
    closest_idx = _binary_search_closest(arr, X)
    low, high = max(closest_idx - K, 0), min(closest_idx + K, len(arr) - 1)
    min_heap = []

    for i in range(low, high + 1):
        item = (abs(arr[i] - X), arr[i])
        heapq.heappush(min_heap, item)

    result = []
    for _ in range(K):
        result.append(heapq.heappop(min_heap)[1])
    result.sort()
    return result


def _binary_search_closest(arr, X):
    if arr[0] >= X:
        return 0
    if arr[-1] <= X:
        return len(arr) - 1

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > X:
            end = mid - 1
        elif arr[mid] < X:
            start = mid + 1
        else:
            return mid

    # arr[start] is bigger than key and arr[end] is smaller
    if (arr[start] - X) > (X - arr[end]):
        return end
    return start


@pytest.mark.parametrize(
    "arr, K, X, expected",
    [
        ([5, 6, 7, 8, 9], 3, 7, [6, 7, 8]),
        ([2, 4, 5, 6, 9], 3, 6, [4, 5, 6]),
        ([2, 4, 5, 6, 9], 3, 10, [5, 6, 9]),
    ],
)
def test_find_closest_elements(arr, K, X, expected):
    assert find_closest_elements(arr, K, X) == expected
