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
  let fastPointer = head;
  let slowPointer = head;

  while (fastPointer !== null && slowPointer !== null) {
    fastPointer = fastPointer?.next?.next;
    slowPointer = slowPointer?.next;

    if (fastPointer === slowPointer) {
      return true;
    }
  }

  return false;
};
