from grokking.two_heaps.utils import MaxHeap, MinHeap


class SlidingWindowMedian:
    """
    Given an array of numbers and a number ‘k’,
    find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
    """

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()

    def _remove_num(self, num):
        heap = self.left if num <= self.left.top() else self.right
        heap.remove(num)
        self._rebalance_heaps()

    def _rebalance_heaps(self):
        """
        left and right heap sizes are equal, or left has 1 more
        """
        len_diff = len(self.left) - len(self.right)
        if len_diff == 2:
            self.right.push(self.left.pop())
        elif len_diff == -1:
            self.left.push(self.right.pop())

    def _insert_num(self, num):
        if len(self.left) == 0 or num <= self.left.top():
            self.left.push(num)
        else:
            self.right.push(num)
        self._rebalance_heaps()

    def _find_median(self):
        if len(self.left) == len(self.right):
            return (self.left.top() + self.right.top()) / 2
        return self.left.top()

    def find_sliding_window_median(self, nums, k):
        ans = []
        window_start = 0
        for window_end in range(len(nums)):
            self._insert_num(nums[window_end])
            if window_end >= k - 1:
                ans.append(self._find_median())
                self._remove_num(nums[window_start])
                window_start += 1
        return ans


def test():
    s1 = SlidingWindowMedian()
    assert s1.find_sliding_window_median([1, 2, -1, 3, 5], 2) == [1.5, 0.5, 1.0, 4.0]

    s2 = SlidingWindowMedian()
    assert s2.find_sliding_window_median([1, 2, -1, 3, 5], 3) == [1.0, 2.0, 3.0]
