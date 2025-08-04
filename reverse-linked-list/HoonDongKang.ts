/**
 * [Problem]: [206] Reverse Linked List
 * (https://leetcode.com/problems/reverse-linked-list/description/)
 */

// Definition for singly-linked list.
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}
function reverseList(head: ListNode | null): ListNode | null {
    // 시간복잡도 O(n)
    // 공간복잡도 O(1)
    let prev: ListNode | null = null;
    let cur = head;
    while (cur) {
        let next = cur.next;
        cur.next = prev;
        prev = cur;
        cur = next;
    }

    return prev;
}
