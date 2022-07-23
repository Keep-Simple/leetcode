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


def reverse_sub_list(head, p, q):
    """
    Given the head of a LinkedList and two positions ‘p’ and ‘q’,
    reverse the LinkedList from position ‘p’ to ‘q’.
    """
    if p == q:
        return head

    curr, prev = head, None
    count = q - p + 1

    while p > 1:
        prev = curr
        curr = curr.next
        p -= 1

    head2 = prev
    tail2 = curr

    while count > 0:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        count -= 1

    if head2:
        head2.next = prev
    else:
        head = prev

    tail2.next = curr

    return head


@pytest.mark.parametrize(
    "head, p, q, expected",
    [
        (
            Node(1, Node(2, Node(3, Node(4, Node(5))))),
            2,
            4,
            Node(1, Node(4, Node(3, Node(2, Node(5))))),
        ),
    ],
)
def test_reverse_sub_list(head, p, q, expected):
    assert reverse_sub_list(head, p, q) == expected
