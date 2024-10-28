class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list
 * T.C. O(N)
 * S.C. O(1)
 */
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let first = head;
  let second = head;

  for (let i = 0; i < n; i++)
    first = first!.next;

  if (!first)
    return head!.next;

  while (first.next) {
    first = first.next;
    second = second!.next;
  }

  second!.next = second!.next!.next;

  return head;
}
