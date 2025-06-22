/**
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1672151418/
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  // dummy 노드를 만들어 head 앞에 두기 (edge case: 첫 번째 노드를 제거할 때 편리)
  let dummy = new ListNode(0);
  dummy.next = head;

  // fast와 slow 포인터를 dummy에서 시작
  let fast = dummy;
  let slow = dummy;

  // fast 포인터를 n+1 만큼 앞으로 이동시킴
  // (slow가 제거 노드의 바로 이전 노드에 멈추도록 하기 위함)
  for (let i = 0; i < n + 1; i++) {
    fast = fast.next;
  }

  // fast와 slow를 함께 끝까지 이동
  while (fast !== null) {
    fast = fast.next;
    slow = slow.next;
  }

  // slow.next가 제거할 노드이므로, 그 노드를 skip
  slow.next = slow.next.next;

  // dummy.next가 새 head
  return dummy.next;
};
