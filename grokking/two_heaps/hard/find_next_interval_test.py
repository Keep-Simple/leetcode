import pytest

from grokking.two_heaps.utils import MinHeap


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    """
    Given an array of intervals,
    find the next interval of each interval.
    In a list of intervals, for an interval ‘i’
    its next interval ‘j’ will have the smallest ‘start’
    greater than or equal to the ‘end’ of ‘i’.

    Write a function to return an array containing indices
    of the next interval of each input interval.
    If there is no next interval of a given interval, return -1.
    It is given that none of the intervals have the same start point.
    """
    starts_heap = MinHeap([[intervals[i].start, i] for i in range(len(intervals))])
    ends_heap = MinHeap([[intervals[i].end, i] for i in range(len(intervals))])
    result = [-1] * len(intervals)

    for _ in range(len(intervals)):
        while len(starts_heap) and starts_heap.top()[0] < ends_heap.top()[0]:
            starts_heap.pop()
        if len(starts_heap):
            result[ends_heap.pop()[1]] = starts_heap.top()[1]
        else:
            break

    return result


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([Interval(2, 3), Interval(3, 4), Interval(5, 6)], [1, 2, -1]),
        ([Interval(3, 4), Interval(1, 5), Interval(4, 6)], [2, -1, -1]),
        ([Interval(1, 4), Interval(2, 3), Interval(3, 4)], [-1, 2, -1]),
    ],
)
def test_find_next_interval(intervals, expected):
    assert find_next_interval(intervals) == expected
