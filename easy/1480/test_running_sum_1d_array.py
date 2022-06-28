from typing import List, Tuple

import pytest
from running_sum_1d_array import Solution


@pytest.fixture
def input_output() -> List[Tuple[List, List]]:
    return [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ]


def test_solution(input_output: List[Tuple[List, List]]) -> None:
    solution = Solution()
    for input, output in input_output:
        assert solution.runningSum(input) == output
