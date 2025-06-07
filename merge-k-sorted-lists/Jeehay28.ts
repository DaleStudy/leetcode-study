class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// TC: O(n * log n), n = total number of all nodes combined (across all lists)
// SC: O(n)
// TDDO: Implement more optimized solution using Min Heap with TC: O(n log k)
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  const nodeValues: number[] = [];

  for (let node of lists) {
    while (node) {
      nodeValues.push(node.val);
      node = node.next;
    }
  }

  nodeValues.sort((a, b) => a - b);

  if (nodeValues.length === 0) return null;

  const head = new ListNode(nodeValues[0]);
  let temp = head;

  for (let i = 1; i < nodeValues.length; i++) {
    temp.next = new ListNode(nodeValues[i]);
    temp = temp.next;
  }

  return head;
}

