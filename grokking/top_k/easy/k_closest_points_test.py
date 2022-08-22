import heapq
import math

import pytest


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance_to_origin = math.sqrt(x**2 + y**2)

    # invert logic to use in heap
    def __lt__(self, other):
        return self.distance_to_origin > other.distance_to_origin


def find_closest_points(points, k):
    """
    Given an array of points in a 2D
    plane, find ‘K’ closest points to the origin.
    """
    max_heap = []

    for i in range(k):
        heapq.heappush(max_heap, Point(*points[i]))

    for i in range(k, len(points)):
        p = Point(*points[i])
        if p.distance_to_origin < max_heap[0].distance_to_origin:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, p)

    return list(map(lambda e: [e.x, e.y], max_heap))


@pytest.mark.parametrize(
    "points, k, expected",
    [
        ([[1, 2], [1, 3]], 1, [[1, 2]]),
        ([[1, 3], [3, 4], [2, -1]], 2, [[1, 3], [2, -1]]),
    ],
)
def test_find_closest_points(points, k, expected):
    assert find_closest_points(points, k) == expected
