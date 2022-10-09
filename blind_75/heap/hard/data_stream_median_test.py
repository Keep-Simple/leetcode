import heapq

"""
https://leetcode.com/problems/find-median-from-data-stream

The median is the middle value in an ordered integer list.
If the size of the list is even,
there is no middle value and the median is the mean of the two middle values.

MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far.

Answers within 10^-5 of the actual answer will be accepted.
"""


class MedianFinder:
    def __init__(self):
        self.left_part = []
        self.right_part = []

    def _parts_diff(self):
        return len(self.left_part) - len(self.right_part)

    def addNum(self, num):
        belongs_to_left_part = num <= -self.left_part[0] if self.left_part else True

        if belongs_to_left_part:
            heapq.heappush(self.left_part, -num)
        else:
            heapq.heappush(self.right_part, num)

        match self._parts_diff():
            case 2:
                heapq.heappush(self.right_part, -heapq.heappop(self.left_part))
            case -1:
                heapq.heappush(self.left_part, -heapq.heappop(self.right_part))

    def findMedian(self):
        if not self.left_part:
            return None

        if self._parts_diff() == 0:
            return (-self.left_part[0] + self.right_part[0]) / 2

        return -self.left_part[0]


def test_funcname():
    median_finder = MedianFinder()
    median_finder.addNum(1)  # arr = [1]
    median_finder.addNum(2)  # arr = [1, 2]
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)  # arr[1, 2, 3]
    assert median_finder.findMedian() == 2.0
