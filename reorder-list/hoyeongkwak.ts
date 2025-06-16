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

/**
 Do not return anything, modify head in-place instead.
 */
 /*
Time complexity: O(N)
Space complexity: O(1)
*/
function reorderList(head: ListNode | null): void {
    let slow = head
    let fast = head
    while (fast && fast.next) {
        slow = slow.next
        fast = fast.next.next
    }
    let curr = slow.next
    slow.next = null
    let prev = null

    while (curr) {
        let temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    }
    let first = head
    let second = prev

    while (second) {
        let firstNext = first.next
        let secondNext = second.next
        first.next = second
        second.next = firstNext
        first = firstNext
        second = secondNext
    }
};
