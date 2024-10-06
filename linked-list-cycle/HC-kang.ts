class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * https://leetcode.com/problems/linked-list-cycle
 * T.C. O(n)
 * S.C. O(n)
 */
function hasCycle(head: ListNode | null): boolean {
    const SET = new Set<ListNode>();
    while (head) {
        if (SET.has(head)) return true;
        SET.add(head);
        head = head.next
    }
    return false;
};

/**
 * T.C. O(n)
 * S.C. O(1)
 */
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
};
