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
  // 리스트가 비었을 때 다른 리스트 반환
  if (list1 === null) return list2;
  if (list2 === null) return list1;

  // 작은 값 가진 노드 선택하고 재귀호출
  if (list1.val <= list2.val) {
    list1.next = mergeTwoLists(list1.next, list2);
    return list1;
  } else {
    list2.next = mergeTwoLists(list1, list2.next);
    return list2;
  }
};

// 시간 복잡도: O(n1+n2)
// 공간 복잡도: O(1)
