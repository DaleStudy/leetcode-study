/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * 주어진 두 연결 리스트를 하나의 정렬 리스트로 병합해 반환하는 함수
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
const mergeTwoLists = function (list1, list2) {
    let head = new ListNode(-1, null);
    let mergedList = head;

    let node1 = list1;
    let node2 = list2;

    while (node1 && node2) {
        if (node1.val >= node2.val) {
            mergedList.next = node2;
            node2 = node2.next;
        } else if (node1.val < node2.val) {
            mergedList.next = node1;
            node1 = node1.next;
        }

        mergedList = mergedList.next;
    }

    mergedList.next = node1 ?? node2;

    return head.next;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
