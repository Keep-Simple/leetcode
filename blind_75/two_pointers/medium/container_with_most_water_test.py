import pytest


def max_area(height):
    """
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints
    of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container,
    such that the container contains the most water.

    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    Solution:
        TC: O(N)
        SC: O(1)

    https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
    """
    n = len(height)
    left, right = 0, n - 1
    max_area = 0

    while left < right:
        min_h = min(height[left], height[right])
        max_area = max(max_area, min_h * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


@pytest.mark.parametrize(
    "height, expected",
    [
        (
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            49,
        ),
        (
            [1, 1],
            1,
        ),
        ([1, 8, 1000, 2, 5, 1000, 8, 3, 7], 3000),
    ],
)
def test_max_area(height, expected):
    assert max_area(height) == expected
