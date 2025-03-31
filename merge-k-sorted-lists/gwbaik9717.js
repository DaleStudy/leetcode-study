// k: len(lists), n: Total number of nodes
// Time complexity: O(nlogk)
// Space complexity: O(n)

class MinHeap {
  constructor() {
    this.heap = [null];
  }

  isEmpty() {
    return this.heap.length === 1;
  }

  push(listNode) {
    this.heap.push(listNode);

    let current = this.heap.length - 1;
    let parent = Math.floor(current / 2);

    while (parent !== 0) {
      if (this.heap[parent].val > listNode.val) {
        [this.heap[parent], this.heap[current]] = [
          this.heap[current],
          this.heap[parent],
        ];

        current = parent;
        parent = Math.floor(current / 2);
        continue;
      }

      break;
    }
  }

  pop() {
    if (this.heap.length === 1) {
      return;
    }

    if (this.heap.length === 2) {
      return this.heap.pop();
    }

    const rv = this.heap[1];

    this.heap[1] = this.heap.pop();

    let current = 1;
    let left = current * 2;
    let right = left + 1;

    while (
      (this.heap[left] && this.heap[current].val > this.heap[left].val) ||
      (this.heap[right] && this.heap[current].val > this.heap[right].val)
    ) {
      if (this.heap[left] && this.heap[right]) {
        if (this.heap[left].val < this.heap[right].val) {
          [this.heap[left], this.heap[current]] = [
            this.heap[current],
            this.heap[left],
          ];
          current = left;
        } else {
          [this.heap[right], this.heap[current]] = [
            this.heap[current],
            this.heap[right],
          ];
          current = right;
        }

        left = current * 2;
        right = left + 1;
        continue;
      }

      [this.heap[left], this.heap[current]] = [
        this.heap[current],
        this.heap[left],
      ];
      current = left;
      left = current * 2;
      right = left + 1;
    }

    return rv;
  }
}

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  const minHeap = new MinHeap();

  for (const list of lists) {
    if (list) {
      minHeap.push(list);
    }
  }

  let answer = null;
  let next = null;

  while (!minHeap.isEmpty()) {
    const current = minHeap.pop();

    if (!answer) {
      answer = new ListNode();
      next = answer;
    }

    next.val = current.val;

    if (current.next) {
      minHeap.push(current.next);
    }

    if (!minHeap.isEmpty()) {
      next.next = new ListNode();
      next = next.next;
    }
  }

  return answer;
};
