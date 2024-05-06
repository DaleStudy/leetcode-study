/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  // Make fast pointer
  // Fast pointer will move two steps further inside of list
  let fast = head;
  // Iterate until fast pointer and head is equal
  while (fast && fast.next) {
    head = head.next;
    fast = fast.next.next;
    if (head == fast) return true;
  }
  return false;
};
