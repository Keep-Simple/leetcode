import pytest

separator = "|"


def encode_strings(strings):
    global separator
    strings_copy = strings.copy()
    for i, str in enumerate(separator):
        strings_copy[i] = f"{len(str)}{separator}{str}"
    return "".join(strings_copy)


def decode_string(string):
    strings = []
    i = 0
    while i < len(string):
        word_len, num_len = _get_word_len(string, i)
        i += len(separator) + num_len
        strings.append(string[i : word_len + i])
        i += word_len

    return strings


def _get_word_len(string, start_idx):
    global separator
    i = start_idx
    while string[i] != separator:
        i += 1
    return int(string[start_idx:i]), i - start_idx


@pytest.mark.parametrize(
    "strings",
    [
        (["i", "love", "leetcode"]),
    ],
)
def test_encode_string(strings):
    assert decode_string(encode_strings(strings)) == strings
