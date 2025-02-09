/**
 * 206. Reverse Linked List
 * Given the head of a singly linked list, reverse the list, and return the reversed list.
 *
 * https://leetcode.com/problems/reverse-linked-list/description/
 *
 */

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

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// O(n) time
// O(1) space
function reverseList(head: ListNode | null): ListNode | null {
  let prev: ListNode | null = null;
  let next: ListNode | null = null;

  while (head) {
    next = head.next;
    head.next = prev;

    prev = head;
    head = next;
  }

  return prev;
}
