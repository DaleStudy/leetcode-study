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
//! 추후 복습 필요한 문제
const mergeTwoLists = function (list1, list2) {
  // 이 부분을 제한 시간 내에 떠올리지 못해 ai로부터 힌트를 받아 로직을 작성
  let temp = new ListNode(0);
  let cur = temp;

  while (list1 !== null && list2 !== null) {
    if (list1.val <= list2.val) {
      cur.next = list1;
      list1 = list1.next;
    } else {
      cur.next = list2;
      list2 = list2.next;
    }
    cur = cur.next;
  }

  cur.next = list1 !== null ? list1 : list2;

  return temp.next;
};
