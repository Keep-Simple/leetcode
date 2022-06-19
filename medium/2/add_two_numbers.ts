export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val
        this.next = next === undefined ? null : next
    }
}

export function addTwoNumbers(l1: ListNode, l2: ListNode): ListNode {
    const resultListNode = new ListNode()
    let currentNode = resultListNode

    while (l1 || l2) {
        const val = (l1?.val || 0) + (l2?.val || 0) + currentNode.val

        currentNode.next = new ListNode(Math.floor(val / 10))
        currentNode.val = val % 10

        l1 = l1?.next
        l2 = l2?.next

        if (l1 || l2 || currentNode.next.val) {
            currentNode = currentNode.next
        } else {
            currentNode.next = null
        }
    }

    return resultListNode
}
