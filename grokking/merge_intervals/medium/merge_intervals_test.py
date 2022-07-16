import pytest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, comp):
        return self.start == comp.start and self.end == comp.end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def merge(intervals):
    """
    Given a list of intervals,
    merge all the overlapping intervals to produce a list
    that has only mutually exclusive intervals.
    """
    intervals.sort(key=lambda i: i.start)

    merged = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start, end = interval.start, interval.end

    merged.append(Interval(start, end))
    return merged


@pytest.mark.parametrize(
    "intervals, expected",
    [
        (
            [Interval(1, 4), Interval(2, 5), Interval(7, 9)],
            [Interval(1, 5), Interval(7, 9)],
        ),
        (
            [Interval(6, 7), Interval(2, 4), Interval(5, 9)],
            [Interval(2, 4), Interval(5, 9)],
        ),
        (
            [Interval(1, 4), Interval(2, 6), Interval(3, 5)],
            [Interval(1, 6)],
        ),
    ],
)
def test(intervals, expected):
    assert merge(intervals) == expected
