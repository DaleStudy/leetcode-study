/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
/*
Time complexity: O(n)
Space complexity: O(h)
*/
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    if (head == null) return head
    const listLength = (node: ListNode | null): number => {
        if (node == null) return 0
        return 1 + listLength(node.next)
    }
    const nodeLen = listLength(head)
    let dummy: ListNode = new ListNode(0, head);
    let node = dummy
    for (let i = 0; i < nodeLen - n; i++) {
        if (node.next) {
            node = node.next
        }
    }
    node.next = node.next.next
    return dummy.next
};
