import pytest


def partition_shots(shots):
    idx_map = {}
    intervals = []

    for i in range(len(shots)):
        if shots[i] in idx_map:
            idx_map[shots[i]][1] = i
        else:
            idx_map[shots[i]] = [i, None]

    for i in range(len(shots)):
        if shots[i] in idx_map:
            s = idx_map[shots[i]]
            intervals.append((s[0], s[1] or s[0]))
            del idx_map[shots[i]]

    merged = merge_intervals(intervals)

    ans = []
    for i in range(len(merged)):
        interval_length = merged[i][1] - merged[i][0] + 1
        ans.append(interval_length)
    return ans


# it's already sorted by start
def merge_intervals(intervals):
    if not intervals:
        return []

    start, end = intervals[0]
    merged = []
    for i in range(len(intervals) - 1):
        interval_start, interval_end = intervals[i]
        if interval_start >= end:
            merged.append((start, end))
            start = interval_start
            end = interval_end
        else:
            end = max(interval_end, end)

    merged.append((start, end))
    return merged


@pytest.mark.parametrize(
    "shots, expected",
    [
        (["a", "b", "c"], [1, 1, 1]),
        (["a", "b", "c", "a"], [4]),
        (
            [
                "a",
                "b",
                "a",
                "b",
                "c",
                "b",
                "a",
                "c",
                "a",
                "d",
                "e",
                "f",
                "e",
                "g",
                "d",
                "e",
                "h",
                "i",
                "j",
                "h",
                "k",
                "l",
                "i",
                "j",
            ],
            [9, 7, 8],
        ),
    ],
)
def test_partition_shots(shots, expected):
    assert partition_shots(shots) == expected
