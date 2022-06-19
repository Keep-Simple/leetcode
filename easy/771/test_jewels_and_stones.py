from typing import Sequence, Tuple

import pytest
from jewels_and_stones import Solution


@pytest.fixture
def data_and_expected() -> Sequence[Tuple[str, str, int]]:
    return [("aA", "aAAbbbb", 3), ("z", "ZZ", 0)]


def test_solution(data_and_expected: Sequence[Tuple[str, str, int]]) -> None:
    solution = Solution()
    for jewels, stones, count in data_and_expected:
        assert solution.numJewelsInStones(jewels, stones) == count
