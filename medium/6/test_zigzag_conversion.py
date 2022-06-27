from typing import List, Tuple

import pytest
from zigzag_conversion import Solution


@pytest.fixture
def input_output() -> List[Tuple[Tuple[str, int], str]]:
    return [
        (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
        (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
        (("A", 1), "A"),
    ]


def test_solution(input_output: List[Tuple[List, List]]) -> None:
    solution = Solution()
    for input, output in input_output:
        assert solution.convert(*input) == output
