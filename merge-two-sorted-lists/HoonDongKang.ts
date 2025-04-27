/**
 * [Problem]: [21] Merge Two Sorted Lists
 *
 * (https://leetcode.com/problems/merge-two-sorted-lists/description/)
 */

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    //시간복잡도 O(m+n)
    //공간복잡도 O(1)
    function loopFunc(list1: ListNode | null, list2: ListNode | null): ListNode | null {
        let current: ListNode = new ListNode();
        let dummy = current;

        while (list1 !== null && list2 !== null) {
            if (list1.val < list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }

            current = current.next;
        }

        current.next = list1 !== null ? list1 : list2;

        return dummy.next;
    }

    //시간복잡도 O(m+n)
    //공간복잡도 O(m+n)
    function recursionFunc(list1: ListNode | null, list2: ListNode | null): ListNode | null {
        if (list1 === null) return list2;
        if (list2 === null) return list1;

        if (list1.val < list2.val) {
            list1.next = recursionFunc(list1.next, list2);
            return list1;
        } else {
            list2.next = recursionFunc(list1, list2.next);
            return list2;
        }
    }

    return recursionFunc(list1, list2);
}
