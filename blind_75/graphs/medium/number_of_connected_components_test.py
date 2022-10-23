from collections import defaultdict

import pytest


def count_components(n, edges):
    """
    https://youtube.com/embed/8f1XPm4WOUc

    Graph of n nodes. Integer n and edges array
    Return the number of connected components in the graph

    Solution:
        Implement union find

        parents[i] is showing parent for node(i)
        rank is for maintaining balanced parent child tree (tree is inside parents array)
        (when union merges two sets we pick head with higher rank)
        components_count is initially at max value = n

        Idea:
            iterate over edges, trying to merge n1 and n2
            if they have same highest parent (find function finds them)
            -> they are already
            is same union, otherwise merge them by chaning parents
            array and upating ranks array (just optimizations)
            after each merge decrement components_count by 1
            return components_count

    TC:
        C - edges count
        N - nodes count
        O(C * alpha(N)):
            alpha - inverse Ackermann function
            union function: O(alpha(N)) applied C times
            due to searching in +-balanced tree (tree is balanced because of ranks optimization, during merge, pick higher rank root)
            and path compaction in find function (step 2 nodes at a time)
    SC:
        O(N) - for storing parents and ranks array


    Union find is less efficient than dfs for static graph
    It shines when graph is dynamic, because we need to run only union function once
    dfs will run all over again
    """
    parents = list(range(n))
    ranks = [1] * n

    def find(n1):
        res = n1
        while res != parents[res]:
            # optmization for speed, works without this line
            parents[res] = parents[parents[res]]
            res = parents[res]
        return res

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return 0

        if ranks[p2] > ranks[p1]:
            parents[p1] = p2
            ranks[p2] += ranks[p1]
        else:
            parents[p2] = p1
            ranks[p1] += ranks[p2]
        return 1

    components_count = n
    for a, b in edges:
        components_count -= union(a, b)

    return components_count


def count_components_dfs(n, edges):
    adj_list = defaultdict(list)

    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = set()

    def dfs(node):
        visited.add(node)
        for child in adj_list[node]:
            if child not in visited:
                dfs(child)

    components_count = 0

    for node in range(n):
        if node not in visited:
            dfs(node)
            components_count += 1

    return components_count


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [[0, 1], [1, 2], [3, 4]], 2),
    ],
)
def test_count_components(n, edges, expected):
    assert count_components(n, edges) == expected
    assert count_components_dfs(n, edges) == expected
