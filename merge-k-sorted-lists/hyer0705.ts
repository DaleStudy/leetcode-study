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

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  if (!lists || lists.length === 0) return null;

  const minHeap = new PriorityQueue((a: ListNode, b: ListNode) => a.val - b.val);

  for (const node of lists) {
    if (node) minHeap.enqueue(node);
  }

  const dummyHead = new ListNode();
  let current = dummyHead;

  while (!minHeap.isEmpty()) {
    const minimumElement = minHeap.dequeue();

    current.next = minimumElement;
    current = current.next;

    if (minimumElement.next) {
      minHeap.enqueue(minimumElement.next);
    }
  }

  return dummyHead.next;
}
