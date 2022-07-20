import heapq

import pytest


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


def min_meeting_rooms(meetings):
    """
    Given a list of intervals representing the start
    and end time of ‘N’ meetings,
    find the minimum number of rooms required to hold all the meetings.


    We can conclude that we need to keep track of the ending time
    of all the meetings currently happening so that
    when we try to schedule a new meeting, we can see
    what meetings have already ended.
    We need to put this information in a data structure
    that can easily give us the smallest ending time.
    A Min Heap would fit our requirements best.
    """
    meetings.sort(key=lambda m: m.start)
    active_meetings = []
    rooms = 0

    for meeting in meetings:
        # remove all meetings that have ended before current one
        while active_meetings and active_meetings[0].end <= meeting.start:
            heapq.heappop(active_meetings)
        heapq.heappush(active_meetings, meeting)
        # heap always has overlapping meetings,
        # amount of overlaps = rooms count
        rooms = max(rooms, len(active_meetings))

    return rooms


@pytest.mark.parametrize(
    "meetings, expected",
    [
        ([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)], 2),
        ([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)], 2),
        ([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)], 1),
        ([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)], 2),
    ],
)
def test(meetings, expected):
    assert min_meeting_rooms(meetings) == expected
