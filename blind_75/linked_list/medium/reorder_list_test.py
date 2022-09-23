import pytest

from blind_75.linked_list.utils import (array_to_linked_list,
                                        linked_list_to_array)


def reorder_list(head):
    """
    You are given the head of a singly linked-list.

    The list can be represented as:
        L0 → L1 → … → L(n - 1) → Ln
    Reorder the list to be on the following form:
        L0 → Ln → L1 → L(n - 1) → L2 → L(n - 2) → …

    You may not modify the values in the list's nodes.
    Only nodes themselves may be changed.
    """


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 2, 3, 4], [1, 4, 2, 4]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ],
)
def test_reorder_list(head, expected):
    assert linked_list_to_array(reorder_list(array_to_linked_list(head))) == expected
