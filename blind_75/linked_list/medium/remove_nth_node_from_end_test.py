import pytest

from blind_75.linked_list.utils import (array_to_linked_list,
                                        linked_list_to_array)


def remove_nth_from_end(head, n):
    """
    Given the head of a linked list,
    remove the nth node from the end of the list and return its head.

    Follow up: Could you do this in one pass?

    Solution:
        1 Setup two pointers, first -> 0, second -> n
        2 Iterate them at the same time until the end (while second and second.next)
        3 Connect first.next with first.next.next, let the garbage collector clean up
    """
    # 1
    p_1 = p_2 = head
    for _ in range(n):
        p_2 = p_2.next

    # n is equal to the list len, change head
    if not p_2:
        return head.next

    # 2
    while p_2 and p_2.next:
        p_2 = p_2.next
        p_1 = p_1.next

    # 3
    p_1.next = p_1.next.next

    return head


@pytest.mark.parametrize(
    "head, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
    ],
)
def test_remove_nth_from_end(head, n, expected):
    assert (
        linked_list_to_array(remove_nth_from_end(array_to_linked_list(head), n))
        == expected
    )
