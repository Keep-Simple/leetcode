import heapq


class KthLargestNumberInStream:
    """
    Design a class to efficiently find
    the Kth largest element in a stream of numbers.

    The class should have the following two things:

    The constructor of the class should accept an integer array
    containing initial numbers from the stream and an integer ‘K’.
    The class should expose a function add(int num)
    which will store the given number and return the Kth largest number.
    """

    def __init__(self, nums, k):
        self.k = k
        min_heap = []
        self.min_heap = min_heap
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                self._add_num(num)

    def _add_num(self, num):
        if self.min_heap[0] < num:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, num)

    def add(self, num):
        if not self.min_heap:
            return -1
        self._add_num(num)
        return self.min_heap[0]


def test():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    assert kthLargestNumber.add(6) == 5
    assert kthLargestNumber.add(13) == 6
    assert kthLargestNumber.add(4) == 6
