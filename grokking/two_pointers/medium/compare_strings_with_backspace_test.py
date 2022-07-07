import pytest


def backspace_compare(str1, str2):
    """
    Given two strings containing backspaces (identified by the character ‘#’),
    check if the two strings are equal.
    """
    pointer1, pointer2 = len(str1) - 1, len(str2) - 1

    while min(pointer1, pointer2) >= 0:
        pointer1 = apply_backspaces(str1, pointer1)
        pointer2 = apply_backspaces(str2, pointer2)

        if pointer1 < 0 and pointer2 < 0:
            return True  # both reached the end
        if pointer1 < 0 ^ pointer2 < 0:
            return True  # only one reached the end
        if str1[pointer1] != str2[pointer2]:
            return False

        pointer1 -= 1
        pointer2 -= 1

    return True


def apply_backspaces(string, ptr):
    backspace_count = 0
    while backspace_count >= 0 and ptr >= 0:
        if string[ptr] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        ptr -= 1

    return ptr


@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("xy#z", "xzz#", True),
        ("xy#z", "xyz#", False),
        ("xp#", "xyz#", False),
        ("xywrrmp", "xywrrmu#p", True),
        ("xp#", "xyz##", True),
        ("xp#p#", "xz#f#", True),
    ],
)
def test(str1, str2, expected):
    assert backspace_compare(str1, str2) == expected
