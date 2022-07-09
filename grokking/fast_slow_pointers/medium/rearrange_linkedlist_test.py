from typing import Optional


class Node:
    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value), end="->")
            temp = temp.next
        print()


def reorder(head):
    """
    Given the head of a Singly LinkedList,
    write a method to modify the LinkedList such that the nodes
    from the second half of the LinkedList are inserted alternately
    to the nodes from the first half in reverse order.
    So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null,
    your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

    Your algorithm should not use any extra space
    and the input LinkedList should be modified in-place.
    """
    if not head or not head.next:
        return

    medium = find_medium(head)
    second_head = reverse_list(medium)

    return merge_lists(head, second_head)


def find_medium(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_lists(head1, head2):
    new_head = head1

    while head2 and head1:
        temp = head1.next
        temp2 = head2.next
        head1.next = head2
        head2.next = temp
        head2 = temp2
        head1 = temp

    if head1:
        head1.next = None

    return new_head


def reverse_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def test():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    reorder(head)
    assert head.value == 2
    assert head.next.value == 10
    assert head.next.next.value == 4
    assert head.next.next.next.value == 8
    assert head.next.next.next.next.value == 6
    assert head.next.next.next.next.next is None
