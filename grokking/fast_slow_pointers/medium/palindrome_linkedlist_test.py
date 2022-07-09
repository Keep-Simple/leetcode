from typing import Optional


class Node:
    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    """
    Given the head of a Singly LinkedList,
    write a method to check if the LinkedList is a palindrome or not.

    Your algorithm should use constant space
    and the input LinkedList should be in the original form.
    The algorithm should have O(N) time complexity
    where ‘N’ is the number of nodes in the LinkedList.

    Solution:
    - Find middle node
    - Reverse from middle to the end
    - Check for palidrome
    - Reverse back
    """
    if not head or not head.next:
        return True

    middle = find_middle(head)

    second_head = reverse_list(middle)

    ptr1, ptr2 = head, second_head
    is_palindrome = True
    while ptr2 and ptr1:
        if ptr1.value != ptr2.value:
            is_palindrome = False
            break
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    reverse_list(second_head)
    return is_palindrome


def print_list(head):
    temp = head
    while temp:
        print(temp.value, end="->")
        temp = temp.next
    print()


def reverse_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def test():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    assert is_palindromic_linked_list(head) is True

    head.next.next.next.next.next = Node(2)
    assert is_palindromic_linked_list(head) is False

    assert is_palindromic_linked_list(None) is True
    assert is_palindromic_linked_list(Node(1)) is True
