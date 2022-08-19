import pytest


def robot_positions_valid(rows, robots_count):
    prev_row = rows[0]
    for i in range(1, len(rows)):
        if not _check_2_rows(prev_row, rows[i], robots_count):
            return False
        prev_row = rows[i]
    return True


def _check_2_rows(row1, row2, robots_count):
    count = 0
    latest_idx = -1
    for i in range(len(row2)):
        if row2[i] == 1:
            count += 1
            is_valid = False
            for j in range(-1, 2):
                if i + j >= 0 and row1[i + j] == 1 and i + j != latest_idx:
                    latest_idx = i + j
                    is_valid = True
                    break
            if not is_valid:
                return False

    return robots_count == count


@pytest.mark.parametrize(
    "grid, robots_count, expected",
    [
        ([[1, 0, 0, 1], [0, 1, 1, 0]], 2, True),
        ([[1, 0, 0, 0, 1], [1, 0, 1, 0, 0]], 2, False),
        ([[1, 0, 0, 1], [1, 1, 0, 0]], 2, False),
    ],
)
def test_robot_positions_valid(grid, robots_count, expected):
    assert robot_positions_valid(grid, robots_count) == expected
