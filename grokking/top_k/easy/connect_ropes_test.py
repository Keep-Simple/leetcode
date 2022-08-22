import heapq

import pytest


def min_cost_to_connect_ropes(ropes):
    """
    Given ‘N’ ropes with different lengths,
    we need to connect these ropes into one big rope with minimum cost.
    The cost of connecting two ropes is equal to the sum of their lengths.
    """
    if not ropes:
        return 0

    min_heap = [*ropes]
    heapq.heapify(min_heap)
    cost = 0

    while len(min_heap) != 1:
        connected_ropes = heapq.heappop(min_heap) + heapq.heappop(min_heap)
        cost += connected_ropes
        heapq.heappush(min_heap, connected_ropes)

    return cost


@pytest.mark.parametrize(
    "rope_length, expected",
    [
        (
            [1, 3, 11, 5],
            33,
        ),  # First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)
        ([3, 4, 5, 6], 36),
        ([1, 3, 11, 5, 2], 42),
    ],
)
def test_min_cost_to_connect_ropes(rope_length, expected):
    assert min_cost_to_connect_ropes(rope_length) == expected
