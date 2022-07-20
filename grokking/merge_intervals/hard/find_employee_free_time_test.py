from heapq import heappop, heappush

import pytest


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class EmployeeInterval:
    def __init__(self, interval, employee_idx, interval_idx):
        # interval representing employee's working hours
        self.interval = interval
        # index of the list containing working hours of this employee
        self.employee_idx = employee_idx
        # index of the interval in the employee list
        self.interval_idx = interval_idx

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    """
    For ‘K’ employees,
    we are given a list of intervals representing
    the working hours of each employee.
    Our goal is to find out if there is a free interval
    that is common to all employees.
    You can assume that each list of employee
    working hours is sorted on the start time.

    Time complexity:
    The above algorithm’s time complexity is O(N*logK)
    where ‘N’ is the total number of intervals,
    and ‘K’ is the total number of employees.
    This is because we are iterating through the intervals only once
    (which will take O(N)), and every time we process an interval,
    we remove (and can insert) one interval in the Min Heap,
    (which will take O(logK)).
    At any time, the heap will not have more than ‘K’ elements.

    Space complexity
    The space complexity of the above algorithm will be O(K)
    as at any time, the heap will not have more than ‘K’ elements.
    """
    if not schedule:
        return []

    result, min_heap = [], []

    # insert the first interval of each employee to the queue
    for i in range(len(schedule)):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    prev_interval = min_heap[0].interval
    while min_heap:
        queue_top = heappop(min_heap)
        # if prev_interval is not overlapping with the next interval, insert a free interval
        if prev_interval.end < queue_top.interval.start:
            result.append(Interval(prev_interval.end, queue_top.interval.start))
            prev_interval = queue_top.interval
        else:  # overlapping intervals, update the prev_interval if needed
            if prev_interval.end < queue_top.interval.end:
                prev_interval = queue_top.interval

        # if there are more intervals available for the same employee, add their next interval
        employee_schedule = schedule[queue_top.employee_idx]
        if len(employee_schedule) > queue_top.interval_idx + 1:
            heappush(
                min_heap,
                EmployeeInterval(
                    employee_schedule[queue_top.interval_idx + 1],
                    queue_top.employee_idx,
                    queue_top.interval_idx + 1,
                ),
            )

    return result


@pytest.mark.parametrize(
    "schedule, expected",
    [
        (
            [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]],
            [Interval(3, 5)],
        ),
        (
            [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]],
            [Interval(4, 6), Interval(8, 9)],
        ),
        (
            [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]],
            [Interval(5, 7)],
        ),
    ],
)
def test(schedule, expected):
    assert find_employee_free_time(schedule) == expected
