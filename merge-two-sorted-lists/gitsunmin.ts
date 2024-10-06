/**
 * https://leetcode.com/problems/merge-two-sorted-lists
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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    if (!list1 && !list2) return null;
    if (!list1) return list2;
    if (!list2) return list1;

    const dummy = new ListNode();
    let current = dummy;

    while (list1 && list2) {
        if (list1.val < list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }

    current.next = list1 || list2;

    return dummy.next;
};

const input1 = new ListNode(1, new ListNode(2, new ListNode(4)));
const input2 = new ListNode(1, new ListNode(3, new ListNode(4)));

console.log('output1:', mergeTwoLists(input1, input2));
console.log('output2:', mergeTwoLists(input2, input1));
