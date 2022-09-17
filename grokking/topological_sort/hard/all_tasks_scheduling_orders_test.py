import pytest


def get_all_topological_sorts(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which need to be completed
    before it can be scheduled. Given the number of tasks
    and a list of prerequisite pairs, write a method to print all
    possible ordering of tasks meeting all prerequisites.


    Solution:
    - build adjacency list and in_degree (incoming edges count for each node)
    - maintain sources array, containing nodes with 0 in_degree
    - multiple sources means that we can peek any and have different topological sorts,
        so using Backtracking to get topo sort for all current sources,
        and then revert in_degree with sorted_order (containing current topo sort)


    TC and SC:
    If we don’t have any prerequisites, all combinations of the tasks can represent a topological ordering.
    As we know, that there can be N! combinations for ‘N’ numbers,
    therefore the time and space complexity of our algorithm will be O(V! * E)
    where ‘V’ is the total number of tasks and ‘E’ is the total prerequisites.
    We need the ‘E’ part because in each recursive call, at max, we remove (and add back) all the edges.


    Similar solution - https://www.geeksforgeeks.org/all-topological-sorts-of-a-directed-acyclic-graph/
        Without keeping sources,
        just iterating through in_degree looking for 0 each time, and keeping visited nodes
    """
    if tasks <= 0:
        return False

    adj_list = {}
    in_degree = {}

    for node in range(tasks):
        adj_list[node] = []
        in_degree[node] = 0

    for src, dest in prerequisites:
        adj_list[src].append(dest)
        in_degree[dest] += 1

    sorted_order = []
    all_sorted_orders = []
    sources = [node for node in in_degree if in_degree[node] == 0]
    _all_topological_sorts(
        adj_list, in_degree, sorted_order, all_sorted_orders, sources
    )
    return all_sorted_orders


def _all_topological_sorts(
    adj_list, in_degree, sorted_order, all_sorted_orders, sources
):
    for source in sources:
        # get the node's children to decrement their in-degrees
        next_sources = list(filter(lambda s: s != source, sources))
        sorted_order.append(source)
        for child in adj_list[source]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                next_sources.append(child)

        # recursive call the remaining (and new) sources
        _all_topological_sorts(
            adj_list, in_degree, sorted_order, all_sorted_orders, next_sources
        )

        # backtrack, remove the vertex from the sorted order and put all of its children back to consider
        # the next source instead of the current vertex
        sorted_order.pop()
        for child in adj_list[source]:
            in_degree[child] += 1

    # if sorted_order doesn't contain all tasks, either we've a cyclic dependency between tasks, or
    # we have not processed all the tasks in this recursive call
    if len(sorted_order) == len(in_degree):
        all_sorted_orders.append(list(sorted_order))


@pytest.mark.parametrize(
    "tasks, prerequisites, expected",
    [
        (3, [[0, 1], [1, 2]], [[0, 1, 2]]),
        (4, [[3, 2], [3, 0], [2, 0], [2, 1]], [[3, 2, 0, 1], [3, 2, 1, 0]]),
        (
            6,
            [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]],
            [
                [0, 1, 4, 3, 2, 5],
                [0, 1, 3, 4, 2, 5],
                [0, 1, 3, 2, 4, 5],
                [0, 1, 3, 2, 5, 4],
                [1, 0, 3, 4, 2, 5],
                [1, 0, 3, 2, 4, 5],
                [1, 0, 3, 2, 5, 4],
                [1, 0, 4, 3, 2, 5],
                [1, 3, 0, 2, 4, 5],
                [1, 3, 0, 2, 5, 4],
                [1, 3, 0, 4, 2, 5],
                [1, 3, 2, 0, 5, 4],
                [1, 3, 2, 0, 4, 5],
            ],
        ),
        (3, [[0, 1], [1, 2], [2, 0]], []),
    ],
)
def test_get_all_topological_sorts(tasks, prerequisites, expected):
    assert sorted(get_all_topological_sorts(tasks, prerequisites)) == sorted(expected)
