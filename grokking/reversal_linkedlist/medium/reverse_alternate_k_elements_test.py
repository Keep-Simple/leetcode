import pytest


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def __eq__(self, other):
        if other is None:
            return False
        return self.value == other.value and self.next == other.next


def reverse_alternate_k_elements(head, k):
    """
    Given the head of a LinkedList and a number ‘k’,
    reverse every alternating ‘k’ sized sub-list starting from the head.

    If, in the end, you are left with a sub-list with less than ‘k’ elements,
    reverse it too.
    """
    if not head or k < 2:
        return head

    curr, prev = head, None
    while curr is not None:
        i = 0
        tail_of_sub = curr
        tail_of_prev_sub = prev

        # reverse k elements
        while curr and i < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        # stich with prev part
        if tail_of_prev_sub:
            tail_of_prev_sub.next = prev
        else:
            head = prev
        # stich with next part
        tail_of_sub.next = curr

        # skip next k elements
        i = 0
        while i < k and curr:
            prev = curr
            curr = curr.next
            i += 1

    return head


@pytest.mark.parametrize(
    "head, k, expected",
    [
        (
            Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8)))))))),
            2,
            Node(2, Node(1, Node(3, Node(4, Node(6, Node(5, Node(7, Node(8)))))))),
        ),
    ],
)
def test_reverse_alternate_k_elements(head, k, expected):
    assert reverse_alternate_k_elements(head, k) == expected
