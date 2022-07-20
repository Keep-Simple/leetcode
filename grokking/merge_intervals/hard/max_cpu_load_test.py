import heapq

import pytest


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end


def find_max_cpu_load(jobs):
    """
    We are given a list of Jobs.
    Each job has a Start time,
    an End time, and a CPU load when it is running.
    Our goal is to find the maximum CPU load
    at any time if all the jobs are running on the same machine.
    """
    jobs.sort(key=lambda j: j.start)
    curr_jobs = []
    max_load = curr_load = 0
    for job in jobs:
        while curr_jobs and curr_jobs[0].end <= job.start:
            curr_load -= heapq.heappop(curr_jobs).cpu_load
        heapq.heappush(curr_jobs, job)
        curr_load += job.cpu_load
        max_load = max(max_load, curr_load)

    return max_load


@pytest.mark.parametrize(
    "jobs, expected",
    [
        ([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)], 7),
        ([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)], 15),
        ([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)], 8),
    ],
)
def test(jobs, expected):
    assert find_max_cpu_load(jobs) == expected
