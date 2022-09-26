import heapq

import pytest

from blind_75.linked_list.utils import (ListNode, array_to_linked_list,
                                        linked_list_to_array)


class ProxyNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other_node):
        return self.node.val < other_node.node.val


def merge_k_sorted_lists(lists):
    """
    You are given an array of k linked-lists lists,
    each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Solution:
        Insert each first node from k lists into the min-heap
        Pop one node at a time from min-heap
            Append it to the result linkedlist
            Insert next node from the same list into the heap
    """
    min_heap = []
    for list_head in lists:
        if list_head:
            heapq.heappush(min_heap, ProxyNode(list_head))

    dummy_head = tail = ListNode()
    while min_heap:
        min_node = heapq.heappop(min_heap)
        tail.next = min_node.node
        tail = tail.next
        if min_node.node.next:
            heapq.heappush(min_heap, ProxyNode(min_node.node.next))

    tail.next = None
    return dummy_head.next


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ],
)
def test_merge_k_sorted_lists(lists, expected):
    assert (
        linked_list_to_array(merge_k_sorted_lists(map(array_to_linked_list, lists)))
        == expected
    )
