// last test case failed
// Time complexity: O(logn)
// Space complexity: O(n)

class MinHeap {
  constructor() {
    this.heap = [null];
  }

  get root() {
    if (this.length === 1) {
      return null;
    }

    return this.heap[1];
  }

  get length() {
    return this.heap.length;
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

var MedianFinder = function () {
  this.leftMinHeap = new MinHeap();
  this.rightMinHeap = new MinHeap();
};

/**
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function (num) {
  const rightMinValue = this.rightMinHeap.root;

  if (num >= rightMinValue) {
    this.rightMinHeap.push(num);
  } else {
    this.leftMinHeap.push(num * -1);
  }

  if (this.rightMinHeap.length - this.leftMinHeap.length > 1) {
    const popped = this.rightMinHeap.pop();
    this.leftMinHeap.push(popped * -1);
  }

  if (this.leftMinHeap.length - this.rightMinHeap.length > 1) {
    const popped = this.leftMinHeap.pop();
    this.rightMinHeap.push(popped * -1);
  }
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function () {
  const len = this.leftMinHeap.length + this.rightMinHeap.length;

  if (len % 2 === 0) {
    return (this.leftMinHeap.root * -1 + this.rightMinHeap.root) / 2;
  }

  if (this.leftMinHeap.length > this.rightMinHeap.length) {
    return this.leftMinHeap.root * -1;
  }

  return this.rightMinHeap.root;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
