/**
 * TC: O(N)
 * SC: O(1)
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let pointer = null;

  while (head) {
    // 1. 정답 리스트의 맨 앞에 새로운 노드를 추가
    pointer = new ListNode(head.val, pointer);
    // 2. head는 다음 노드로 이동
    head = head.next;
  }

  return pointer;
};
