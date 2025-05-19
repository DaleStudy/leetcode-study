/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val === undefined ? 0 : val);
 *     this.next = (next === undefined ? null : next);
 * }
 */

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  // 1) 가짜 시작점(dummy)과 current 포인터 생성
  const dummy = new ListNode(-1);
  let current = dummy;

  // 2) 두 리스트 모두 남아 있는 동안 더 작은 노드를 연결
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

  // 3) 남은 노드를 한 번에 이어붙이고, 결과 반환
  current.next = list1 || list2;
  return dummy.next;
};
