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
var mergeTwoLists = function (list1, list2) {
  let dummy = new ListNode(-1); // 임시 노드
  let current = dummy;

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

  // 남은 노드들 붙이기
  current.next = list1 !== null ? list1 : list2;

  return dummy.next; // dummy는 가짜니까 next부터가 진짜 head
};
// 시간 복잡도: O(n + m) (n: list1의 길이, m: list2의 길이)
// 공간 복잡도: O(1) (dummy 노드 하나만 사용)
