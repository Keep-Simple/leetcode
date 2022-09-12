import pytest


def get_all_topological_sorts(tasks, prerequisites):
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which need to be completed
    before it can be scheduled. Given the number of tasks
    and a list of prerequisite pairs, write a method to print all
    possible ordering of tasks meeting all prerequisites.
    """


@pytest.mark.parametrize(
    "tasks, prerequisites, expected",
    [
        (3, [[0, 1], [1, 2]], [0, 1, 2]),
        (4, [3, 2], [3, 0], [2, 0], [2, 1], [[3, 2, 0, 1], [3, 2, 1, 0]]),
        (
            6,
            [2, 5],
            [0, 5],
            [0, 4],
            [1, 4],
            [3, 2],
            [1, 3],
            [
                [0, 1, 4, 3, 2, 5],
                [0, 1, 3, 4, 2, 5],
                [0, 1, 3, 2, 4, 5],
                [0, 1, 3, 2, 5, 4],
                [1, 0, 3, 4, 2, 5],
                [1, 0, 3, 2, 4, 5],
                [1, 0, 3, 2, 5, 4],
                [1, 0, 4, 3, 2, 5],
                [1, 3, 0, 2, 4, 5],
                [1, 3, 0, 2, 5, 4],
                [1, 3, 0, 4, 2, 5],
                [1, 3, 2, 0, 5, 4],
                [1, 3, 2, 0, 4, 5],
            ],
        ),
    ],
)
def test_get_all_topological_sorts(tasks, prerequisites, expected):
    assert get_all_topological_sorts(tasks, prerequisites) == expected
