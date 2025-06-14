class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 Do not return anything, modify head in-place instead.
 */

// TC: O(n)
// SC: O(n)
function reorderList(head: ListNode | null): void {
  const nodes: ListNode[] = [];

  while (head) {
    nodes.push(head);
    head = head.next;
  }

  let start = 0;
  let end = nodes.length - 1;

  while (start < end) {
    nodes[start].next = nodes[end];
    start++;
    if (start === end) break;
    nodes[end].next = nodes[start];
    end--;
  }

  nodes[start].next = null;
}
