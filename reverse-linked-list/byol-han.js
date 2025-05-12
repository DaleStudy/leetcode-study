/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * https://leetcode.com/problems/reverse-linked-list/
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let prev = null;
  let current = head;

  while (current) {
    const next = current.next; // 다음 노드 기억
    current.next = prev; // 현재 노드가 이전 노드를 가리키도록 변경
    prev = current; // prev를 현재 노드로 이동
    current = next; // current를 다음 노드로 이동
  }

  return prev; // prev는 새로운 head
};
