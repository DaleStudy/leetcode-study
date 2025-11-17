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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  if (!head) return null;

  let current = head;
  let nodeLen = 0;
  while (current.next) {
    current = current.next;
    nodeLen++;
  }

  if (nodeLen - n < 0) return head.next;

  current = head;
  let count = 0;
  while (count < nodeLen - n) {
    current = current.next;
    count++;
  }
  current.next = current.next.next;

  return head;
}
