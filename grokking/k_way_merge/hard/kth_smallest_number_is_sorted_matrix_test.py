from heapq import heappop, heappush

import pytest


# tried to use the fact that columns are sorted too
# by moving row down or column right
# can be further optimized to add only the min move
# requires additional set for tracking visited cells
def find_kth_smallest(matrix, k):
    """
    Given an N * N matrix
    where each row and column is sorted in ascending order,
    find the Kth smallest element in the matrix.
    """
    n = len(matrix) - 1
    min_heap = []

    heappush(min_heap, (matrix[0][0], 0, 0))
    visited = set()

    i = 0
    while min_heap:
        val, row_idx, column_idx = heappop(min_heap)
        if i == k - 1:
            return val

        moves = [[1, 0], [0, 1]]

        for _x, _y in moves:
            y, x = row_idx + _y, column_idx + _x
            if y <= n and x <= n:
                if (y, x) not in visited:
                    heappush(
                        min_heap,
                        (matrix[y][x], y, x),
                    )
                    visited.add((y, x))

        i += 1


# simple merge-k list, don't use the fact that columns are sorted too
def find_kth_smallest_2(matrix, k):
    """
    First, we inserted at most ‘K’ or one element from each of the ‘N’ rows,
    which will take O(min(K, N))
    Then we went through at most ‘K’ elements in the matrix and remove/add
    one element in the heap in each step.
    As we can’t have more than ‘N’ elements
    in the heap in any condition, therefore, the overall time complexity
    of the above algorithm will be O(min(K, N) + K*logN)
    .
    """
    n = len(matrix)
    min_heap = []

    for i in range(min(n, k)):
        if matrix[i]:
            heappush(min_heap, (matrix[i][0], i, 0))

    i = 0
    while min_heap:
        val, row_idx, column_idx = heappop(min_heap)
        if i == k - 1:
            return val
        if column_idx + 1 < n:
            heappush(
                min_heap, (matrix[row_idx][column_idx + 1], row_idx, column_idx + 1)
            )
        i += 1


# binary search on a "number" range (not idx)
def find_kth_smallest_3(matrix, k):
    """
    The Binary Search could take O(log(max-min ))
    iterations where ‘max’ is the largest and ‘min’
    is the smallest element in the matrix and in each iteration we take O(N)
    for counting, therefore, the overall time
    complexity of the algorithm will be O(N*log(max-min))
    """
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = (end + start) / 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower

    return start


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            # as matrix[row][col] is bigger than the mid, let's keep track of the
            # smallest number greater than the mid
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            # as matrix[row][col] is less than or equal to the mid, let's keep track of the
            # biggest number less than or equal to the mid
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger


@pytest.mark.parametrize(
    "matrix, k, expected",
    [
        (
            [
                [2, 6, 8],
                [3, 7, 10],
                [5, 8, 11],
            ],
            5,
            7,
        ),
        (
            [
                [2, 4, 8],
                [3, 7, 10],
                [5, 8, 11],
            ],
            5,
            7,
        ),
        (
            [
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15],
            ],
            8,
            13,
        ),
        (
            [
                [1, 3, 5],
                [6, 7, 12],
                [11, 14, 14],
            ],
            6,
            11,
        ),
        (
            [
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15],
            ],
            8,
            13,
        ),
    ],
)
def test_find_kth_smallest(matrix, k, expected):
    assert find_kth_smallest(matrix, k) == expected
    assert find_kth_smallest_2(matrix, k) == expected
    assert find_kth_smallest_3(matrix, k) == expected
