class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// TC: O(n)
// SC: O(1)
function reverseList(head: ListNode | null): ListNode | null {
  if (!head) return head;

  //         1 -> 2 -> 3 -> 4 -> 5 -> null

  // null <- 1
  // prev   curr

  // null <- 1 <- 2
  //       prev  cur

  let prev: ListNode | null = null;
  let curr: ListNode | null = head;

  while (curr) {
    const tempNext: ListNode | null = curr.next; // 2 -> 3 -> 4 -> 5 -> null
    curr.next = prev; // curr: 1 -> null
    prev = curr; // curr: 1 -> null, 2 -> 1 -> null
    curr = tempNext;
  }

  return prev;
}
