/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    // 결과 리스트의 시작점을 위한 더미 노드
    let dummy = new ListNode(-1);
    let current = dummy;

    // 둘 다 null이 아닐 때까지 반복
    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }

    // 남은 노드가 있으면 그대로 붙임
    current.next = list1 !== null ? list1 : list2;

    return dummy.next; // dummy 다음이 진짜 head
};
