// ✅ Time Complexity: O(N)
// ✅ Space Complexity: O(N) (due to the stack storage)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
  let stack = [];
  let node = head;

  while (node) {
    stack.push(node);
    node = node.next;
  }

  let dummy = new ListNode(-1);
  node = dummy;

  const len = stack.length;

  for (let i = 0; i < len; i++) {
    if (i % 2 === 1) {
      node.next = stack.pop();
    } else {
      node.next = head;
      head = head.next;
    }
    node = node.next;
  }

  node.next = null;
  return dummy.next;
};

