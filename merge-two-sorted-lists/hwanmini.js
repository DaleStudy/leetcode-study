// m: list1, n: list2
// 시간복잡도: O(m + n)
// 공간복잡도: O(m + n)

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
    let res = new ListNode()
    let resCopy = res

    while (list1 && list2) {
        if (list1.val < list2.val) {
            res.next = list1
            list1 = list1.next;
        } else {
            res.next = list2
            list2 = list2.next;
        }

        res = res.next
    }

    if (list1) res.next = list1;
    if (list2) res.next = list2

    return resCopy.next
};

