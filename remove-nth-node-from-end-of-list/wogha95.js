/**
 * TC: O(N)
 * SC: O(1)
 * N: list length
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
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  let listLength = 0;
  let pointer = head;

  while (pointer) {
    pointer = pointer.next;
    listLength += 1;
  }

  // if target of removal is the first node in list
  if (listLength === n) {
    return head.next;
  }

  let nextCount = listLength - n - 1;
  pointer = head;

  while (nextCount) {
    pointer = pointer.next;
    nextCount -= 1;
  }

  pointer.next = pointer.next.next;

  return head;
};
