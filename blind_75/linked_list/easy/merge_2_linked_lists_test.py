import pytest

from blind_75.linked_list.utils import (ListNode, array_to_linked_list,
                                        linked_list_to_array)


def merge_two_lists(list1, list2):
    """
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a one sorted list.
    The list should be made by splicing together
    the nodes of the first two lists.

    Return the head of the merged linked list.
    """
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    # get real head
    return dummy.next


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_merge_two_lists(list1, list2, expected):
    assert (
        linked_list_to_array(
            merge_two_lists(array_to_linked_list(list1), array_to_linked_list(list2))
        )
        == expected
    )
