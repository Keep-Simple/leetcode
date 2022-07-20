import pytest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, comp):
        return self.start == comp.start and self.end == comp.end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def can_attend_all_appointments(intervals):
    """
    Given an array of intervals representing ‘N’ appointments,
    find out if a person can attend all the appointments.

    In Simple words find out if there is an overlap
    """
    intervals.sort(key=lambda i: i.start)

    for i in range(1, len(intervals)):
        # not <= because, == is not an overlap
        if intervals[i].start < intervals[i - 1].end:
            return False
    return True


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([Interval(1, 4), Interval(2, 5), Interval(7, 9)], False),
        ([Interval(6, 7), Interval(2, 4), Interval(8, 12)], True),
        ([Interval(4, 5), Interval(2, 3), Interval(3, 6)], False),
    ],
)
def test(intervals, expected):
    assert can_attend_all_appointments(intervals) == expected
