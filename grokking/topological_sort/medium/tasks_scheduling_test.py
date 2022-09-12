from collections import defaultdict, deque
from enum import Enum

import pytest


def is_schedulling_possible(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks
    which need to be completed before it can be scheduled.
    Given the number of tasks and a list of prerequisite pairs,
    find out if it is possible to schedule all the tasks.
    """
    if tasks <= 0:
        return False

    graph = {}
    in_degree = {}
    for node in range(tasks):
        graph[node] = []
        in_degree[node] = 0
    for _in, _out in prerequisites:
        in_degree[_out] += 1
        graph[_in].append(_out)

    ans = []
    # can be stack also
    queue = deque()

    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        ans.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return len(ans) == tasks


class Color(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


def is_scheduling_possible_dfs(tasks, prerequisites):
    # Create the adjacency list representation of the graph
    adj_list = defaultdict(list)

    for src, dest in prerequisites:
        adj_list[src].append(dest)

    topological_sorted_order = []
    is_possible = True

    # By default all vertces are WHITE
    color = {k: Color.WHITE for k in range(tasks)}

    def dfs(node):
        nonlocal is_possible
        # Don't recurse further if we found a cycle already
        if not is_possible:
            return

        # Start the recursion
        color[node] = Color.GRAY

        # Traverse on neighboring vertices
        if node in adj_list:
            for child in adj_list[node]:
                match color[child]:
                    case Color.WHITE:
                        dfs(child)
                    case Color.GRAY:
                        # An edge to a GRAY vertex represents a cycle
                        is_possible = False

        # Recursion ends. We mark it as black
        color[node] = Color.BLACK
        topological_sorted_order.append(node)

    for vertex in range(tasks):
        # If the node is unprocessed, then call dfs on it.
        if color[vertex] == Color.WHITE:
            dfs(vertex)

    # return topological_sorted_order[::-1] if is_possible else []
    return is_possible


@pytest.mark.parametrize(
    "tasks, prerequisites, expected",
    [
        (3, [[0, 1], [1, 2]], True),
        (3, [[0, 1], [1, 2], [2, 0]], False),
        (6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]], True),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 2]], False),
    ],
)
def test_is_schedulling_possible(tasks, prerequisites, expected):
    assert is_schedulling_possible(tasks, prerequisites) == expected
    assert is_scheduling_possible_dfs(tasks, prerequisites) == expected
