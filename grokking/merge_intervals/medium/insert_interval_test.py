from operator import attrgetter

import pytest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, comp):
        return self.start == comp.start and self.end == comp.end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def insert(intervals, new_interval):
    """
    Given a list of non-overlapping intervals sorted by their start time,
    insert a given interval at the correct position
    and merge all necessary intervals to produce a list
    that has only mutually exclusive intervals.
    """
    i, merged = 0, []
    start, end = attrgetter("start", "end")(new_interval)

    while i < len(intervals) and intervals[i].end < start:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i].start <= end:
        start = min(intervals[i].start, start)
        end = max(intervals[i].end, end)
        i += 1

    merged.append(Interval(start, end))

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


@pytest.mark.parametrize(
    "intervals, new_interval, expected",
    [
        (
            [Interval(1, 3), Interval(5, 7), Interval(8, 12)],
            Interval(4, 6),
            [Interval(1, 3), Interval(4, 7), Interval(8, 12)],
        ),
        (
            [Interval(1, 3), Interval(5, 7), Interval(8, 12)],
            Interval(4, 10),
            [Interval(1, 3), Interval(4, 12)],
        ),
        (
            [Interval(2, 3), Interval(5, 7)],
            Interval(1, 4),
            [Interval(1, 4), Interval(5, 7)],
        ),
    ],
)
def test(intervals, new_interval, expected):
    assert insert(intervals, new_interval) == expected
