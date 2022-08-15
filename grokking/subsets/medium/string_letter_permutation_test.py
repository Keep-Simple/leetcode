import pytest


def find_letter_case_string_permutations(str):
    """
    Given a string,
    find all of its permutations preserving
    the character sequence but changing case.
    """
    permutations = [str]

    for i in range(len(str)):
        if str[i].isalpha():
            for j in range(len(permutations)):
                copy = list(permutations[j])
                copy[i] = copy[i].swapcase()
                permutations.append("".join(copy))

    return permutations


@pytest.mark.parametrize(
    "str, expected",
    [
        ("ab7c", ["ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]),
        ("ad52", ["ad52", "Ad52", "aD52", "AD52"]),
    ],
)
def test_find_letter_case_string_permutations(str, expected):
    assert find_letter_case_string_permutations(str) == expected
