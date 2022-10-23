from collections import defaultdict

import pytest


def is_valid_tree(n, edges):
    """
    Given n nodes (0 to n-1) and undirected edges
    Check if these edges make up a valid TREE
    No duplicate edges

    Solution:
        Firstly check if edges count is n-1 (because it's tree with n nodes)
        (there is no duplicates from the description)
        Look for cycle, if it exists return False

        Run dfs from any node, remembering visited
        if len(visited) != n -> tree isn't valid

        If graph has a cycle, that means that we have >1 components inside
        graph (because there is only n-1 edges), so visited will have less than n
    """
    if len(edges) != n - 1:
        return False

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

    dfs(0)

    return len(visited) == n


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    ],
)
def test_is_valid_tree(n, edges, expected):
    assert is_valid_tree(n, edges) == expected
