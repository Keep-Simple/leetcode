import pytest

from blind_75.linked_list.utils import (array_to_linked_list,
                                        linked_list_to_array)


def has_cycle(head):
    """
    Given head, the head of a linked list,
    determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is
    some node in the list that can be reached again by continuously following the next pointer.
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
    Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list.
    Otherwise, return false.
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


@pytest.mark.parametrize(
    "head, expected",
    [],
)
def test_has_cycle(head, expected):
    assert linked_list_to_array(has_cycle(array_to_linked_list(head))) == expected
