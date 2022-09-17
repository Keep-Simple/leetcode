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
    """
    Given the head of a Singly LinkedList, reverse the LinkedList.
    Write a function to return the new head of the reversed LinkedList.

    Solution:
        To reverse a LinkedList, we need to reverse one node at a time.
        We will start with a variable current which will initially point to the head of the LinkedList
        and a variable previous which will point to the previous node that we have processed;
        initially previous will point to null.

        In a stepwise manner, we will reverse the current node by pointing it to the previous before moving on to the next node.
        Also, we will update the previous to always point to the previous node that we have processed.
    """
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
