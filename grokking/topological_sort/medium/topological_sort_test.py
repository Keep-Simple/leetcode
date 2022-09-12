from collections import deque
from enum import Enum

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

    # can be stack also
    sources = deque()
    # Find all sources i.e., all vertices with 0 in-degrees
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # For each source, add it to the sorted_order
    # and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        # get the node's children to decrement their in-degrees
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []

    return sorted_order


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


def topological_sort_dfs(vertices, edges):
    """
    DFS approach - https://leetcode.com/problems/course-schedule-ii/solution/
    """
    if vertices <= 0:
        return []

    graph = {}
    state = {}
    for i in range(vertices):
        graph[i] = []
        state[i] = State.UNVISITED

    for inbound, outbound in edges:
        graph[inbound].append(outbound)

    stack = []
    is_possible = True

    def dfs(node):
        nonlocal is_possible
        if not is_possible:
            return

        state[node] = State.VISITING
        for child in graph[node]:
            match state[child]:
                case State.VISITING:
                    # cycle deteced
                    is_possible = False
                case State.UNVISITED:
                    dfs(child)
        # recursion end, marke as visited
        state[node] = State.VISITED
        stack.append(node)

    for node in graph:
        if state[node] == State.UNVISITED:
            dfs(node)

    # topological sort is not possible as the graph has a cycle
    if is_possible:
        stack.reverse()
        return stack
    else:
        return []


@pytest.mark.parametrize(
    "vertices, edges, expected",
    [
        # (
        #     4,
        #     [[3, 2], [3, 0], [2, 0], [2, 1]],
        #     [3, 2, 0, 1],
        # ),
        # (
        #     5,
        #     [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]],
        #     [4, 2, 3, 0, 1],
        # ),
        # (
        #     7,
        #     [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]],
        #     [5, 6, 3, 4, 0, 2, 1],
        # ),
        (
            3,
            [[0, 1], [1, 2], [2, 0]],
            [],
        ),
    ],
)
def test_topological_sort(vertices, edges, expected):
    assert topological_sort_bfs(vertices, edges) == expected
    # also valid, but outputs another topological sort
    assert topological_sort_dfs(vertices, edges) == expected
