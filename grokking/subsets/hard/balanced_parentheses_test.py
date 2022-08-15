from collections import deque

import pytest


def generate_valid_parentheses(num):
    """
    For a given number ‘N’,
    write a function to generate all combination
    of ‘N’ pairs of balanced parentheses.
    """
    permutations = deque([("", 0, 0)])
    for _ in range(num * 2):
        for _ in range(len(permutations)):
            (
                curr_permutation,
                left_parentheses_count,
                right_parentheses_count,
            ) = permutations.popleft()
            if left_parentheses_count < num:
                permutations.append(
                    (
                        curr_permutation + "(",
                        left_parentheses_count + 1,
                        right_parentheses_count,
                    )
                )
            if right_parentheses_count < left_parentheses_count:
                permutations.append(
                    (
                        curr_permutation + ")",
                        left_parentheses_count,
                        right_parentheses_count + 1,
                    )
                )

    return list(map(lambda p: p[0], permutations))


def generate_valid_parentheses_2(num):
    permutations = deque([("", 0, 0)])
    result = []
    while permutations:
        (
            curr_permutation,
            left_parentheses_count,
            right_parentheses_count,
        ) = permutations.popleft()

        if left_parentheses_count == num and right_parentheses_count == num:
            result.append(curr_permutation)
        else:
            if left_parentheses_count < num:
                permutations.append(
                    (
                        curr_permutation + "(",
                        left_parentheses_count + 1,
                        right_parentheses_count,
                    )
                )
            if right_parentheses_count < left_parentheses_count:
                permutations.append(
                    (
                        curr_permutation + ")",
                        left_parentheses_count,
                        right_parentheses_count + 1,
                    )
                )

    return result


@pytest.mark.parametrize(
    "num, expected",
    [
        (
            2,
            ["(())", "()()"],
        ),
        (
            3,
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        ),
    ],
)
def test_generate_valid_parentheses(num, expected):
    assert generate_valid_parentheses(num) == expected
