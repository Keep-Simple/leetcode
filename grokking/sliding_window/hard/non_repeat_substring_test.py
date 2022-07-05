import pytest


def non_repeat_substring_set(string):
    window_start = 0
    char_set = set()
    max_size = 0

    for window_end in range(len(string)):
        if string[window_end] in char_set:
            while True:
                window_start += 1
                if string[window_start - 1] == string[window_end]:
                    break

        char_set.add(string[window_end])
        max_size = max(max_size, window_end - window_start + 1)
    return max_size


# better solution
def non_repeat_substring(string):
    window_start = 0
    max_size = 0
    char_index_map = {}

    for window_end in range(len(string)):
        char = string[window_end]
        if char in char_index_map:
            window_start = max(window_start, char_index_map[char] + 1)

        char_index_map[char] = window_end
        max_size = max(max_size, window_end - window_start + 1)
    return max_size


@pytest.mark.parametrize(
    "string, expected",
    [
        ("aabccbb", 3),
        ("abbbb", 2),
        ("abccde", 3),
    ],
)
def test(string, expected):
    assert non_repeat_substring(string) == expected
    assert non_repeat_substring_set(string) == expected
