/**
 * https://leetcode.com/problems/reorder-list/
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

function reorderList(head: ListNode | null): void {
    if (!head || !head.next) return;

    // 1. 중간 지점 찾기 (Floyd’s Tortoise and Hare)
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
    }

    // 2. 중간 이후의 리스트 뒤집기
    let prev: ListNode | null = null;
    let curr: ListNode | null = slow;

    while (curr) {
        const next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }

    // 3. 앞부분과 뒤집어진 후반부 병합
    let first: ListNode | null = head;
    let second: ListNode | null = prev;

    while (second && second.next) {
        const temp1 = first!.next;
        const temp2 = second.next;

        first!.next = second;
        second.next = temp1;

        first = temp1;
        second = temp2;
    }
};
