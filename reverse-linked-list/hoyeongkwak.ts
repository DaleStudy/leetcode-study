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
curr                prev
1, 2, 3, 4, 5       null
2, 3, 4, 5          1
3, 4, 5             2, 1
4, 5                3, 2, 1
5                   4, 3, 2, 1
null                5, 4, 3, 2, 1
*/
/*
    time complexity : O(n)
    space complexity : O(1)
*/
function reverseList(head: ListNode | null): ListNode | null {
    let curr = head
    let prev = null
    while (curr) {
        let next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    }
    return prev
};
