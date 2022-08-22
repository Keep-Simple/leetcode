import heapq

import pytest


def schedule_tasks(tasks, k):
    """
    You are given a list of tasks that need to be run,
    in any order, on a server. Each task will take one CPU interval
    to execute but once a task has finished,
    it has a cooling period during which it can’t be run again.
    If the cooling period for all tasks is ‘K’ intervals,
    find the minimum number of CPU intervals
    that the server needs to finish all tasks.

    If at any time the server can’t execute any task then it must stay idle
    """
    # calculate freq_map
    # insert each task to max-heap based on freq
    # try to execute k+1 task (after executing "a", we need k more -> 1 + k)
    # if it was less than k+1 task -> increase interval count
    freq_map = {}
    for task in tasks:
        freq_map[task] = freq_map.get(task, 0) + 1

    max_heap = []
    for task, freq in freq_map.items():
        heapq.heappush(max_heap, (-freq, task))

    queue = []
    i = 0
    while max_heap:
        n = k + 1
        while n > 0 and max_heap:
            freq, task = heapq.heappop(max_heap)
            freq = -freq - 1
            if freq != 0:
                queue.append((-freq, task))
            n -= 1
            i += 1

        while queue:
            heapq.heappush(max_heap, queue.pop())

        if max_heap:
            i += n

    return i


@pytest.mark.parametrize(
    "tasks, k, expected",
    [
        (["a", "a", "a", "b", "c", "c"], 2, 7),  # a -> c -> b -> a -> c -> idle -> a
        (["a", "b", "a"], 3, 5),  # a -> b -> idle -> idle -> a
        (["a", "a", "a", "b", "b", "b"], 0, 6),
        (["a", "a", "a", "b", "b", "b"], 2, 8),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    ],
)
def test_schedule_tasks(tasks, k, expected):
    assert schedule_tasks(tasks, k) == expected
