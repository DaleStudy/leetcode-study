/**
 * [Problem]: [19] Remove Nth Node From End of List
 * (https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
 */

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    // 시간복잡도 O(N)
    // 공간복잡도 O(1)
    function lengthFunc(head: ListNode | null, n: number): ListNode | null {
        let length = 0;
        let current = head;
        while (current) {
            length++;
            current = current.next;
        }

        let dummy = new ListNode(0, head);
        current = dummy;

        for (let i = 0; i < length - n; i++) {
            current = current?.next!;
        }

        current.next = current.next!.next || null;

        return dummy.next;
    }

    // 시간복잡도 O(N)
    // 공간복잡도 O(1)
    function twoPointerFunc(head: ListNode | null, n: number): ListNode | null {
        let first = head;

        for (let i = 0; i < n; i++) {
            first = first?.next!;
        }

        let dummy = new ListNode(0, head);
        let second = dummy;

        while (first) {
            first = first.next;
            second = second.next!;
        }

        second.next = second.next?.next || null;
        return dummy.next;
    }
}
