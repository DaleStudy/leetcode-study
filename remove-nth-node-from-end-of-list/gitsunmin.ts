/**
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 * time complexity : O(n)
 * space complexity : O(1)
 */

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let first: ListNode | null = dummy;
    let second: ListNode | null = dummy;

    for (let i = 0; i <= n; i++) {
        if (first !== null) first = first.next;
    }

    while (first !== null) {
        first = first.next;
        second = second!.next;
    }

    if (second !== null && second.next !== null) second.next = second.next.next;

    return dummy.next;
};
