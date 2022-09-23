import heapq
from collections import defaultdict

import pytest


def top_k_frequent(nums, k):
    """
    Given an integer array nums and an integer k,
    return the k most frequent elements.
    You may return the answer in any order.

    Min Heap soluiton:
        SC:
            O(N) for freq_map, O(K) for min_heap
            K <= N => O(N)
        TC:
            O(N) for generating freq_map, O(N*log(K))

    Could also used Max Heap:
        SC:
            O(N) for max_heap, instead of (K) for min_heap
            Still O(N)
        TC:
            O(N) for heapifying all frequencies + O(K*log(N)) for popping top K

        - better than min heap, but if K is much smaller than N
          in reality uses more memory
    """
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    min_heap = []

    for unique_num in freq_map:
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq_map[unique_num], unique_num))
        elif min_heap[0][0] < freq_map[unique_num]:
            heapq.heapreplace(min_heap, (freq_map[unique_num], unique_num))

    return list(map(lambda v: v[1], min_heap))


def top_k_frequent_bucket_sort(nums, k):
    """
    Solution:
        create array of buckets (other arrays)
        with size len(nums) + 1 (possible frequency range 0 to len(nums))
        where idx is a freqency and values inside buckets are numbers

    SC:
        O(N) for count dict + O(N) for freq buckets
    TC:
        O(N) for generating freq + O(N) for filling freq
        + O(N) for iterating to get top K values = O(N)
    """
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        (
            [3, 0, 1, 0],
            1,
            [0],
        ),
    ],
)
def test_top_k_frequent(nums, k, expected):
    assert sorted(top_k_frequent(nums, k)) == sorted(expected)
    assert sorted(top_k_frequent_bucket_sort(nums, k)) == sorted(expected)
