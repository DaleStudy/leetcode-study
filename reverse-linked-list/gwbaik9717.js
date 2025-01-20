// Time complexity: O(n)
// Space complexity: O(1)

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
  let current = head;
  let prev = null;

  while (current) {
    const node = new ListNode(current.val);
    node.next = prev;
    prev = node;
    current = current.next;
  }

  return prev;
};
