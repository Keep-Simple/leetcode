import pytest


def word_game(word, k):
    if k <= 0:
        return []

    window_start = 0
    chars_map = {}
    repeated_char = (None, None)
    ans = []

    for window_end in range(len(word)):
        curr_char = word[window_end]
        if curr_char in chars_map:
            if repeated_char[0]:
                window_start = chars_map[repeated_char[1]] + 1
            repeated_char = (curr_char, chars_map[curr_char])
        chars_map[curr_char] = window_end

        if window_end >= k - 1:
            if repeated_char[0]:
                ans.append(word[window_start : window_end + 1])
            if window_start == repeated_char[1]:
                repeated_char = (None, None)
            else:
                del chars_map[word[window_start]]
            window_start += 1

    return ans


@pytest.mark.parametrize(
    "word, k, expected",
    [
        ("awaglk", 4, ["awag"]),
        ("awaglak", 4, ["awag", "agla"]),
        ("asfd", 0, []),
    ],
)
def test_word_game(word, k, expected):
    assert word_game(word, k) == expected
