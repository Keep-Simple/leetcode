from typing import Optional


class Node:
    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    """
    Given the head of a Singly LinkedList,
    write a method to return the middle node of the LinkedList.

    If the total number of nodes in the LinkedList is even,
    return the second middle node.
    """
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    assert find_middle_of_linked_list(head).value == 3

    head.next.next.next.next.next = Node(6)
    assert find_middle_of_linked_list(head).value == 4

    head.next.next.next.next.next.next = Node(7)
    assert find_middle_of_linked_list(head).value == 4
