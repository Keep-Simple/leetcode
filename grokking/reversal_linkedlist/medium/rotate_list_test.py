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


def rotate(head, rotations):
    """
    Given the head of a Singly LinkedList and a number ‘k’,
    rotate the LinkedList to the right by ‘k’ nodes.
    """
    if not head or not head.next or rotations <= 0:
        return head

    n = list_len(head)
    rotations = n - (rotations % n)

    tail_1 = head
    while rotations > 1:
        tail_1 = tail_1.next
        rotations -= 1

    curr = tail_1
    while curr and curr.next:
        curr = curr.next

    curr.next = head
    head = tail_1.next
    tail_1.next = None

    return head


def list_len(head):
    counter = 0
    while head:
        head = head.next
        counter += 1
    return counter


@pytest.mark.parametrize(
    "head, rotations, expected",
    [
        (
            Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))),
            3,
            Node(4, Node(5, Node(6, Node(1, Node(2, Node(3)))))),
        ),
        (
            Node(1, Node(2, Node(3, Node(4, Node(5))))),
            8,
            Node(3, Node(4, Node(5, Node(1, Node(2))))),
        ),
    ],
)
def test_rotate(head, rotations, expected):
    assert rotate(head, rotations) == expected
