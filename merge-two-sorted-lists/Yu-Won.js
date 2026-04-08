/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 *
 * 문제: https://leetcode.com/problems/merge-two-sorted-lists/
 * 요구사항: 정의된 ListNode 를 활용해서 정렬된 배열을 리턴
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */


const mergeTwoLists = (list1, list2) => {
    const dummy = new ListNode(0);
    let cur = dummy;

    while (list1 && list2) {
        if (list1.val <= list2.val) {
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
};
