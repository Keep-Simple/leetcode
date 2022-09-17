from collections import defaultdict

import pytest

from grokking.topological_sort.medium.tasks_scheduling_test import deque


def find_trees_brute_force(nodes, edges):
    """
    We are given an undirected graph that has characteristics of a k-ary tree.
    In such a graph, we can choose any node as the root to make a k-ary tree.
    The root (or the tree) with the minimum height will be
    called Minimum Height Tree (MHT). There can be multiple MHTs for a graph.
    In this problem, we need to find all those roots which give us MHTs.
    Write a method to find all MHTs of the given graph and return a list
    of their roots.

    Solution brute-force:
        - build adjacency list for a graph
        - use dfs to find out the max height, starting from every possible node as a root
        - pick the minimum height, print related roots

    TC:
        DFS - O(V+E)
        DFS * V times = O(V^2+EV)
    SC:
        O(V+E), storing all nodes and edges
    """
    adj_list = {node: [] for node in range(nodes)}
    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    max_height_dict = defaultdict(list)

    for node in adj_list:
        visited = set()
        max_height_dict[_dfs_max_len(node, adj_list, visited)].append(node)

    min_height = min(max_height_dict)

    return max_height_dict[min_height]


def _dfs_max_len(node, adj_list, visited, depth=0):
    visited.add(node)
    max_len = 0
    for child in adj_list[node]:
        if child not in visited:
            max_len = max(_dfs_max_len(child, adj_list, visited, depth + 1), max_len)
    return max_len + 1


def find_trees(nodes, edges):
    """
    Trim for the win (treaming leaf nodes level by level, until 1 or 2 nodes left)
    only 2 or 1 MHT are possible
    Read more: https://leetcode.com/problems/minimum-height-trees/solution/
    """
    if nodes <= 2:
        return [node for node in range(nodes)]

    adj_list = {node: [] for node in range(nodes)}

    for node1, node2 in edges:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    leaves = deque([node for node in adj_list if len(adj_list[node]) == 1])
    remaining_nodes = nodes

    # Remove leaves level by level and subtract each leave's children's.
    # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
    # Any node that has already been a leaf cannot be the root of a minimum height tree, because
    # its adjacent non-leaf node will always be a better candidate.
    while remaining_nodes > 2:
        leaves_count_on_current_lvl = len(leaves)
        remaining_nodes -= leaves_count_on_current_lvl
        for _ in range(leaves_count_on_current_lvl):
            leaf = leaves.popleft()
            parent = adj_list[leaf].pop()
            adj_list[parent].remove(leaf)
            if len(adj_list[parent]) == 1:
                leaves.append(parent)

    return list(leaves)


@pytest.mark.parametrize(
    "nodes, edges, expected",
    [
        (5, [[0, 1], [1, 2], [1, 3], [2, 4]], [1, 2]),
        (4, [[0, 1], [0, 2], [2, 3]], [0, 2]),
        (4, [[0, 1], [1, 2], [1, 3]], [1]),
    ],
)
def test_find_trees(nodes, edges, expected):
    assert find_trees_brute_force(nodes, edges) == expected
    assert find_trees(nodes, edges) == expected
