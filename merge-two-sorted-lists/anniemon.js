/**
 * 시간 복잡도:
 *   list1의 길이가 m, list2의 길이가 n이면
 *   포인터가 최대 m + n만큼 순회하므로 O(m + n)
 * 공간 복잡도:
 *   포인터를 사용하므로 O(1)
 */
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
  const head = new ListNode(0, null);
  let pointer = head;
  while(list1 && list2) {
      if(list1.val < list2.val) {
          pointer.next = list1;
          list1 = list1.next;
      } else {
          pointer.next = list2;
          list2 = list2.next;
      }
      pointer = pointer.next;
  }
  if(list1) {
      pointer.next = list1;
  } else {
      pointer.next = list2;
  }
  return head.next;
};
