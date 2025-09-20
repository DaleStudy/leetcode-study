/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

// Runtime: 49ms
// Memory: 56.94MB

function hasCycle(head: ListNode | null): boolean {
  let fast = head;
  let slow = head;

  while (fast && fast.next) {
      fast = fast.next.next;
      slow = slow!.next;

      if (fast === slow) {
          return true;
      }
  }
  return false;
}
