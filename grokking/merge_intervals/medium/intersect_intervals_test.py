import pytest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, comp):
        return self.start == comp.start and self.end == comp.end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def merge(intervals_a, intervals_b):
    """
    Given two lists of intervals,
    find the intersection of these two lists.
    Each list consists of disjoint intervals sorted on their start time.
    """
    result, i_a, i_b = [], 0, 0

    while i_a < len(intervals_a) and i_b < len(intervals_b):
        a, b = intervals_a[i_a], intervals_b[i_b]
        a_overlaps_b = a.start <= b.end and a.end >= b.start
        b_overlaps_a = b.start <= a.end and b.end >= a.start
        if b_overlaps_a or a_overlaps_b:
            result.append(
                Interval(
                    start=max(a.start, b.start),
                    end=min(a.end, b.end),
                )
            )

        if a.end < b.end:
            i_a += 1
        else:
            i_b += 1

    return result


@pytest.mark.parametrize(
    "intervals_a, intervals_b, expected",
    [
        (
            [Interval(1, 3), Interval(5, 6), Interval(7, 9)],
            [Interval(2, 3), Interval(5, 7)],
            [Interval(2, 3), Interval(5, 6), Interval(7, 7)],
        ),
        (
            [Interval(1, 3), Interval(5, 7), Interval(9, 12)],
            [Interval(5, 10)],
            [Interval(5, 7), Interval(9, 10)],
        ),
    ],
)
def test(intervals_a, intervals_b, expected):
    assert merge(intervals_a, intervals_b) == expected
