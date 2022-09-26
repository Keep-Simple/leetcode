import math

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

    Solution:
        1 Split list into 2 lists 0 to ceil(n/2), to n
        2 Reverse 2nd list
        3 Iterate over 2nd list and insert nodes into the 1st
    """
    # 1
    n = _list_len(head)
    if n <= 2:
        return head
    split_point = math.ceil(n / 2)
    tail_1 = _get_nth_in_list(head, split_point - 1)
    head_2 = tail_1.next
    tail_1.next = None

    # 2
    head_2 = _reverse_list(head_2)

    # 3
    return _merge_2_lists(head, head_2)


def _merge_2_lists(head, head_2):
    curr = head
    while head_2:
        temp = curr.next
        temp_2 = head_2.next

        curr.next = head_2
        curr.next.next = temp

        curr = temp
        head_2 = temp_2

    return head


def _reverse_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def _get_nth_in_list(head, n):
    curr = head
    while curr and n > 0:
        curr = curr.next
        n -= 1
    return curr if n == 0 else None


def _list_len(head):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length


def reorder_list_2(head):
    """
    The same approach, but uses slow and fast pointers
    to find the middle of the list (1 iteration instead of 2)
    """
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head_2 = slow.next
    slow.next = None
    head_2 = _reverse_list(head_2)
    return _merge_2_lists(head, head_2)


@pytest.mark.parametrize(
    "head, expected",
    [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ],
)
def test_reorder_list(head, expected):
    assert linked_list_to_array(reorder_list(array_to_linked_list(head))) == expected
    assert linked_list_to_array(reorder_list_2(array_to_linked_list(head))) == expected
