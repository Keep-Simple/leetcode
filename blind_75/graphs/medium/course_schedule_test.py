from collections import defaultdict

import pytest


def can_finish(num_courses, prerequisites):
    """
    https://leetcode.com/problems/course-schedule/

    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi]
    indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.

    Solution:
        Try to build topological sort, if it's possible return True
    """
    in_degree = {i: 0 for i in range(num_courses)}
    adj_list = defaultdict(list)
    for a, b in prerequisites:
        adj_list[a].append(b)
        in_degree[b] += 1

    topo_sort_len = 0
    queue = [n for n in in_degree if in_degree[n] == 0]
    while queue:
        node = queue.pop()
        topo_sort_len += 1
        for child in adj_list[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return topo_sort_len == num_courses


def can_finish_2(num_courses, prerequisites):
    adj_list = defaultdict(list)
    for a, b in prerequisites:
        adj_list[a].append(b)

    visiting = set()

    def dfs(n):
        if n in visiting:
            return False
        if len(adj_list[n]) == 0:
            return True

        visiting.add(n)
        for child in adj_list[n]:
            if not dfs(child):
                return False
        visiting.remove(n)

        adj_list[n].clear()
        return True

    for n in range(num_courses):
        if not dfs(n):
            return False
    return True


@pytest.mark.parametrize(
    "num_courses, prerequisites, expected",
    [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
    ],
)
def test_can_finish(num_courses, prerequisites, expected):
    assert can_finish(num_courses, prerequisites) == expected
    assert can_finish_2(num_courses, prerequisites) == expected
