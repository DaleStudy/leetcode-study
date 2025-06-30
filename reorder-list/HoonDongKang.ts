/**
 * [Problem]: [143] Reorder List
 * (https://leetcode.com/problems/reorder-list/)
 */

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function stackFunc(head: ListNode | null): void {
        if (!head || !head.next) return;

        const stack: ListNode[] = [];
        let node: ListNode | null = head;

        while (node) {
            stack.push(node);
            node = node.next;
        }

        const length = stack.length;
        node = head;

        for (let i = 0; i < Math.floor(length / 2); i++) {
            const tail = stack.pop()!;
            const next: ListNode | null = node.next;

            node.next = tail;
            tail.next = next;

            node = next!;
        }

        node.next = null;
    }
    //시간복잡도 O(n)
    //공간복잡도 O(1)
    function twoPointerFunc(head: ListNode | null): void {
        if (!head || !head.next) return;

        let slow = head;
        let fast = head;
        while (fast && fast.next && fast.next.next) {
            slow = slow.next!;
            fast = fast.next.next;
        }

        let prev: ListNode | null = null;
        let curr = slow.next;
        slow.next = null;

        while (curr) {
            const next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        let first = head;
        let second = prev;

        while (second) {
            const tmp1 = first!.next;
            const tmp2 = second.next;

            first!.next = second;
            second.next = tmp1;

            first = tmp1!;
            second = tmp2;
        }
    }
}
