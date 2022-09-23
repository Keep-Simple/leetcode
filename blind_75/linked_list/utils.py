class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(val=arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(val=arr[i])
        curr = curr.next
    return head


def linked_list_to_array(head):
    if not head:
        return []
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr
