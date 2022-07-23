import pytest
from partial_reverse_sub_list_test import reverse_sub_list


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


def reverse_every_k(head, k):
    """
    Given the head of a LinkedList and a number ‘k’,
    reverse every ‘k’ sized sub-list starting from the head.

    If, in the end, you are left with a sub-list with less than ‘k’ elements,
    reverse it too.
    """
    if k <= 1 or head is None:
        return head

    i, n = 1, list_len(head)
    while i <= n:
        head = reverse_sub_list(head, i, min(i + k - 1, n))
        i += k
    return head


def list_len(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def reverse_every_k_2(head, k):
    if k <= 1 or head is None:
        return head

    curr, prev = head, None

    while True:
        last_of_prev_part = prev
        # after reversing the LinkedList 'current'
        # will become the last node of the sub-list
        last_of_sub_list = curr
        i = 0
        while curr and i < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1

        if last_of_prev_part:
            last_of_prev_part.next = prev
        else:
            # we are changing the first node (head) of the LinkedList
            head = prev

        last_of_sub_list.next = curr

        if not curr:
            break
        prev = last_of_sub_list

    return head


@pytest.mark.parametrize(
    "head, k, expected",
    [
        (
            Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8)))))))),
            3,
            Node(3, Node(2, Node(1, Node(6, Node(5, Node(4, Node(8, Node(7)))))))),
        ),
    ],
)
def test_reverse_sub_list(head, k, expected):
    # assert reverse_every_k(head, k) == expected
    assert reverse_every_k_2(head, k) == expected
