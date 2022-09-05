from collections import deque

import pytest


def topological_sort_bfs(vertices, edges):
    """
    Topological Sort of a directed graph (a graph with unidirectional edges)
    is a linear ordering of its vertices
    such that for every directed edge (U, V)
    from vertex U to vertex V, U comes before V in the ordering.

    Given a directed graph, find the topological ordering of its vertices.
    BFS approach
    """
    sorted_order = []
    if vertices <= 0:
        return sorted_order

    #  Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # Build the graph
    for edge in edges:
        parent, child = edge
        graph[parent].append(child)  # put the child into it's parent's list
        in_degree[child] += 1  # increment child's inDegree

    # Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # For each source, add it to the sorted_rrder
    # and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[
            vertex
        ]:  # get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []

    return sorted_order


def topological_sort_dfs(vertices, edges):
    ...


@pytest.mark.parametrize(
    "vertices, edges, expected",
    [
        (
            4,
            [[3, 2], [3, 0], [2, 0], [2, 1]],
            [3, 2, 0, 1],
        ),
        (
            5,
            [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]],
            [4, 2, 3, 0, 1],
        ),
        (
            7,
            [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]],
            [5, 6, 3, 4, 0, 2, 1],
        ),
    ],
)
def test_topological_sort(vertices, edges, expected):
    assert topological_sort_bfs(vertices, edges) == expected
    assert topological_sort_dfs(vertices, edges) == expected
