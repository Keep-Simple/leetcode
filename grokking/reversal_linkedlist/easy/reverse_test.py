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


def reverse(head):
    """ """
    cursor = head
    prev = None

    while cursor:
        temp = cursor.next
        cursor.next = prev
        prev = cursor
        cursor = temp

    return prev


@pytest.mark.parametrize(
    "head, expected",
    [
        (
            Node(2, Node(4, Node(6, Node(8, Node(10))))),
            Node(10, Node(8, Node(6, Node(4, Node(2))))),
        ),
    ],
)
def test_reverse(head, expected):
    assert reverse(head) == expected
