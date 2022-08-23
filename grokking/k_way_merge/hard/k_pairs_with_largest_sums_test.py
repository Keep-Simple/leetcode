from heapq import heappop, heappush

import pytest


def find_k_largest_pairs(nums1, nums2, k):
    """
    Given two sorted arrays in descending order,
    find ‘K’ pairs with the largest sum where
    each pair consists of numbers from both the arrays.
    """
    ans = []
    max_heap = []

    heappush(max_heap, (-(nums1[0] + nums2[0]), 0, 0))

    i = 0
    while max_heap and i < k:
        _, idx1, idx2 = heappop(max_heap)
        ans.append([nums1[idx1], nums2[idx2]])

        if idx1 + 1 < len(nums1):
            heappush(max_heap, (-(nums1[idx1 + 1] + nums2[idx2]), idx1 + 1, idx2))
        if idx2 + 1 < len(nums2):
            heappush(max_heap, (-(nums1[idx1] + nums2[idx2 + 1]), idx1, idx2 + 1))

        i += 1

    return ans


# suggested solution
def find_k_largest_pairs_2(nums1, nums2, k):
    min_heap = []
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                # if the sum of the two numbers from the two arrays is smaller than the smallest(top)
                # element of the heap, we can 'break' here. Since the arrays are sorted in the
                # descending order, we'll not be able to find a pair with a higher sum moving forward
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:  # we have a pair with a larger sum, remove top and insert this pair in the heap
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))

    result = []
    for _, i, j in min_heap:
        result.append([nums1[i], nums2[j]])

    return result


@pytest.mark.parametrize(
    "nums1, nums2, k, expected",
    [
        (
            [9, 8, 2],
            [6, 3, 1],
            3,
            [[9, 6], [8, 6], [9, 3]],
        ),
        (
            [5, 2, 1],
            [2, -1],
            3,
            [[5, 2], [5, -1], [2, 2]],
        ),
    ],
)
def test_find_k_largest_pairs(nums1, nums2, k, expected):
    assert find_k_largest_pairs(nums1, nums2, k) == expected
    # assert find_k_largest_pairs_2(nums1, nums2, k) == expected
