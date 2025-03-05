// Time complexity: O(nlogn)
// Space complexity: O(n)

class _Queue {
  constructor() {
    this.q = [];
    this.front = 0;
    this.rear = 0;
  }

  push(value) {
    this.q.push(value);
    this.rear++;
  }

  shift() {
    const rv = this.q[this.front];
    delete this.q[this.front++];
    return rv;
  }

  isEmpty() {
    return this.front === this.rear;
  }
}

class MinHeap {
  constructor() {
    this.heap = [null];
  }

  push(value) {
    this.heap.push(value);

    let current = this.heap.length - 1;
    let parent = Math.floor(current / 2);

    while (parent && this.heap[current] < this.heap[parent]) {
      [this.heap[current], this.heap[parent]] = [
        this.heap[parent],
        this.heap[current],
      ];
      current = parent;
      parent = Math.floor(current / 2);
    }
  }

  pop() {
    if (this.heap.length === 1) {
      return null;
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
      (this.heap[left] && this.heap[current] > this.heap[left]) ||
      (this.heap[right] && this.heap[current] > this.heap[right])
    ) {
      if (this.heap[right] && this.heap[right] < this.heap[left]) {
        [this.heap[right], this.heap[current]] = [
          this.heap[current],
          this.heap[right],
        ];
        current = right;
      } else {
        [this.heap[left], this.heap[current]] = [
          this.heap[current],
          this.heap[left],
        ];
        current = left;
      }

      left = current * 2;
      right = left + 1;
    }

    return rv;
  }
}
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
  const minHeap = new MinHeap();

  const q = new _Queue();
  q.push(root);

  while (!q.isEmpty()) {
    const current = q.shift();

    minHeap.push(current.val);

    if (current.left) {
      q.push(current.left);
    }

    if (current.right) {
      q.push(current.right);
    }
  }

  let answer = null;
  for (let i = 0; i < k; i++) {
    answer = minHeap.pop();
  }

  return answer;
};
