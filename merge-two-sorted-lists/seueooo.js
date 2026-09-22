/**
 * 풀이
 * 더 작은 노드를 머리로 두고, 그 next에 나머지를 병합한 결과를 연결.
 * 최종적으로 머리를 반환
 *
 * 시간복잡도 - O(n + m) : n, m은 각각 list1, list2의 길이
 * 공간복잡도 - O(n + m) : 재귀 호출 스택
 *
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
  if (!list1) return list2;
  if (!list2) return list1;

  if (list1.val <= list2.val) {
    list1.next = mergeTwoLists(list1.next, list2);
    return list1;
  } else {
    list2.next = mergeTwoLists(list1, list2.next);
    return list2;
  }
};
