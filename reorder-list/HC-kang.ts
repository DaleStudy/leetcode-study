class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * https://leetcode.com/problems/reorder-list
 * T.C. O(n)
 * S.C. O(1)
 */
function reorderList(head: ListNode | null): void {
  if (!head || !head.next) return;

  let fast: ListNode | null = head;
  let slow: ListNode | null = head;

  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow!.next;
  }

  let prev: ListNode | null = null;
  let curr: ListNode | null = slow;
  while (curr) {
    const next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  let front: ListNode | null = head;
  let back: ListNode | null = prev;
  while (back!.next) {
    const frontNext = front!.next;
    const backNext = back!.next;

    front!.next = back;
    back!.next = frontNext;

    front = frontNext;
    back = backNext;
  }
}
