import pytest

from blind_75.linked_list.utils import (array_to_linked_list,
                                        linked_list_to_array)


def reverse_list(head):
    """
    Given the head of a singly linked list,
    reverse the list, and return the reversed list.
    """
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        (
            [1, 2],
            [2, 1],
        ),
        ([], []),
    ],
)
def test_reverse_list(head, expected):
    assert linked_list_to_array(reverse_list(array_to_linked_list(head))) == expected
