/**
 * [Problem]: [141] Linked List Cycle
 * (https://leetcode.com/problems/linked-list-cycle/description/)
 */
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

function hasCycle(head: ListNode | null): boolean {
    //시간복잡도 O(n)
    //공간복잡도 O(n)
    function setFunc(head: ListNode | null): boolean {
        if (!head) return false;
        const set = new Set<ListNode>();
        let currentNode: ListNode = head;

        while (currentNode) {
            if (set.has(currentNode)) return true;

            set.add(currentNode);
            currentNode = currentNode.next!;
        }

        return false;
    }
    //시간복잡도 O(n)
    //공간복잡도 O(1)
    function pointerFunc(head: ListNode | null): boolean {
        let slow = head;
        let fast = head;
        while (fast && fast.next) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow === fast) return true;
        }
        return false;
    }
}
