import pytest


def are_brackets_balanced(string):
    brackets_stack = []
    for char in string:
        if _is_opening_bracket(char):
            brackets_stack.append(char)
        if _is_closing_bracket(char):
            if not brackets_stack or not _is_matching_brackets(
                brackets_stack[-1], char
            ):
                return 0
            else:
                brackets_stack.pop()

    return 1 if not brackets_stack else 0


def _is_opening_bracket(char):
    return char in "({[<"


def _is_closing_bracket(char):
    return char in ")}]>"


def _is_matching_brackets(br1, br2):
    pairs = ("()", "{}", "[]", "<>")
    return f"{br1}{br2}" in pairs


@pytest.mark.parametrize(
    "string, expected",
    [("()he(<>", 0), ("[](){}<>", 1)],
)
def test_are_brackets_balanced(string, expected):
    assert are_brackets_balanced(string) == expected
