import pytest

parentheses = {
    "(": ")",
    "{": "}",
    "[": "]",
}


def is_valid(s):
    """
    Given a string s containing just the characters
    '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
    """
    stack = []
    for bracket in s:
        if bracket in parentheses:
            stack.append(bracket)
        else:
            if not stack:
                return False
            last_open = stack.pop()
            if parentheses[last_open] != bracket:
                return False

    return len(stack) == 0


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
    ],
)
def test_is_valid(s, expected):
    assert is_valid(s) == expected
