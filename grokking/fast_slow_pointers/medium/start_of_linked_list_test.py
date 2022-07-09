from typing import Optional


class Node:
    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            k = calculate_cycle_length(slow)
            ptr1 = ptr2 = head

            for _ in range(k):  # move ptr2 K ahead of ptr1
                ptr2 = ptr2.next

            while ptr2 != ptr1:  # ptr1 and ptr2 will meet at the cycle start
                ptr1 = ptr1.next
                ptr2 = ptr2.next

            return ptr2

    return None


# Fload's Cycle algo
# https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list
def find_cycle_start_2(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            slow = head
            while slow != fast:  # ptr1 and ptr2 will meet at the cycle start
                slow = slow.next
                fast = fast.next

            return slow

    return None


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    assert find_cycle_start(head).value == 3
    assert find_cycle_start_2(head).value == 3

    head.next.next.next.next.next.next = head.next.next.next
    assert find_cycle_start(head).value == 4
    assert find_cycle_start_2(head).value == 4

    head.next.next.next.next.next.next = head
    assert find_cycle_start(head).value == 1
    assert find_cycle_start_2(head).value == 1
