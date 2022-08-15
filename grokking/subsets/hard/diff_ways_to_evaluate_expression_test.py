import pytest


def diff_ways_to_evaluate_expression(input):
    """
    Given an expression containing digits and operations (+, -, *),
    find all possible ways in which the expression
    can be evaluated by grouping the numbers and operators using parentheses.

    Could be optimized by adding caching with map
    """
    result = []
    has_operators = False
    for i in range(len(input)):
        if input[i] in ["+", "-", "*"]:
            has_operators = True
            left = diff_ways_to_evaluate_expression(input[:i])
            right = diff_ways_to_evaluate_expression(input[i + 1 :])

            for l in left:
                for r in right:
                    result.append(eval(f"{l}{input[i]}{r}"))

    if not has_operators:
        result.append(int(input))

    return result


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1+2*3", [7, 9]),
        ("2*3-4-5", [8, -12, 7, -7, -3]),
    ],
)
def test_diff_ways_to_evaluate_expression(input, expected):
    assert diff_ways_to_evaluate_expression(input) == expected
