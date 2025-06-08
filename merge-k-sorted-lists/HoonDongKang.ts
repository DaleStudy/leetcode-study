/**
 * [Problem]: [23] Merge k Sorted Lists
 * (https://leetcode.com/problems/merge-k-sorted-lists/description/)
 */

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    //시간복잡도: O(n log n)
    //공간복잡도: O(n)
    function bruteForceFunc(lists: Array<ListNode | null>): ListNode | null {
        const arr: number[] = [];
        let dummy = new ListNode(0);
        let current = dummy;

        if (!lists.length) return null;

        for (let i = 0; i < lists.length; i++) {
            let currentNode = lists[i];
            while (currentNode) {
                arr.push(currentNode.val);
                currentNode = currentNode.next;
            }
        }

        arr.sort((a, b) => a - b);

        for (let j = 0; j < arr.length; j++) {
            current.next = new ListNode(arr[j]);
            current = current.next;
        }

        return dummy.next;
    }

    //시간복잡도: O(nk)
    //공간복잡도: O(n)
    function mergeFunc(lists: Array<ListNode | null>): ListNode | null {
        let dummy = new ListNode(0);
        let cur = dummy;

        while (lists.some((node) => node !== null)) {
            let minVal = Infinity;
            let minIdx = -1;

            for (let i = 0; i < lists.length; i++) {
                if (lists[i] && lists[i]!.val < minVal) {
                    minVal = lists[i]!.val;
                    minIdx = i;
                }
            }

            if (minIdx !== -1) {
                cur.next = new ListNode(minVal);
                cur = cur.next;
                lists[minIdx] = lists[minIdx]!.next;
            }
        }

        return dummy.next;
    }
    //시간복잡도: O(n log k)
    //공간복잡도: O(log k)
    function divideAndConqureFunc(lists: Array<ListNode | null>): ListNode | null {
        if (!lists.length) return null;
        if (lists.length === 1) return lists[0];

        const mid = Math.floor(lists.length / 2);
        const left = divideAndConqureFunc(lists.slice(0, mid));
        const right = divideAndConqureFunc(lists.slice(mid));

        function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
            const dummy = new ListNode(-1);
            let cur = dummy;

            while (list1 && list2) {
                if (list1.val < list2.val) {
                    cur.next = list1;
                    list1 = list1.next;
                } else {
                    cur.next = list2;
                    list2 = list2.next;
                }

                cur = cur.next;
            }

            cur.next = list1 ?? list2;
            return dummy.next;
        }

        return mergeTwoLists(left, right);
    }
}
