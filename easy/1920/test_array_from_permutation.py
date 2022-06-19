from typing import List, Tuple

import pytest
from array_from_permutation import Solution

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]],
# nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]


@pytest.fixture
def input_output() -> List[Tuple[List, List]]:
    return [
        ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
        ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3]),
    ]


def test_solution(input_output: List[Tuple[List, List]]) -> None:
    solution = Solution()
    for input, output in input_output:
        assert solution.buildArray([*input]) == output
        assert solution.buildArraySimple([*input]) == output
