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

// using iterative
function reverseList(head: ListNode | null): ListNode | null {
  if (!head) return null;

  let prev: ListNode | null = null;
  let current = head;

  while (current) {
    const temp: ListNode | null = current.next;
    current.next = prev;
    prev = current;
    current = temp;
  }

  return prev;
}

// using recursive
function reverseList(head: ListNode | null): ListNode | null {
  if (!head || !head.next) return head;

  const newHead = reverseList(head.next);

  head.next.next = head;
  head.next = null;

  return newHead;
}
