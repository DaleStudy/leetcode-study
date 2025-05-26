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
function hasCycle(head: ListNode | null): boolean {

  let fast: ListNode | null = head;
  let slow: ListNode | null = head;

  while (fast && fast.next) {
    fast = fast.next.next;

    if (slow !== null) {
      slow = slow.next;
    } else {
      return false;
    }

    if (fast === slow) return true;
  }

  return false;
}


// TC: O(n)
// SC: O(n)
/*
function hasCycle(head: ListNode | null): boolean {

  let dummy: ListNode | null = head;
  const visited = new Set<ListNode>();

  while (dummy) {
    if (visited.has(dummy)) return true;

    visited.add(dummy);

    dummy = dummy.next;
  }

  return false;
}
*/

