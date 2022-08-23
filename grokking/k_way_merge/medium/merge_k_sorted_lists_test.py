import heapq

import pytest


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __eq__(self, other):
        return self.value == other.value and self.next == other.next

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    """
    Given an array of ‘K’ sorted LinkedLists,
    merge them into one sorted list.
    """
    min_heap = []

    for list in lists:
        if list:
            heapq.heappush(min_heap, list)

    result_head, result_tail = None, None

    while min_heap:
        node = heapq.heappop(min_heap)
        if not result_head:
            result_head = node
            result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next
        if node.next:
            heapq.heappush(min_heap, node.next)

    return result_head


@pytest.mark.parametrize(
    "lists, expected",
    [
        (
            [
                ListNode(2, ListNode(6, ListNode(8))),
                ListNode(3, ListNode(6, ListNode(7))),
                ListNode(1, ListNode(3, ListNode(4))),
            ],
            ListNode(
                1,
                ListNode(
                    2,
                    ListNode(
                        3,
                        ListNode(
                            3,
                            ListNode(
                                4,
                                ListNode(
                                    6,
                                    ListNode(6, ListNode(7, ListNode(8))),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ],
)
def test_merge_lists(lists, expected):
    assert merge_lists(lists) == expected
