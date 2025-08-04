class MedianFinder {
  // [1, 2, 3, 4, 5, 6]
  private lower: MaxHeap; // max heap [3, 2, 1]
  private upper: MinHeap; // min heap [4, 5, 6]

  constructor() {
    this.upper = new MinHeap();
    this.lower = new MaxHeap();
  }

  // TC: O(log n)
  // SC: O(n)
  addNum(num: number): void {
    if (this.upper.size() === 0 || this.upper.getRoot() <= num) {
      this.upper.insert(num);
    } else {
      this.lower.insert(num);
    }

    // Balance
    if (this.lower.size() - this.upper.size() > 1) {
      this.upper.insert(this.lower.removeRoot());
    } else if (this.upper.size() - this.lower.size() > 1) {
      this.lower.insert(this.upper.removeRoot());
    }
  }

  // TC: O(1)
  // SC: O(1)
  findMedian(): number {
    if (this.upper.size() === this.lower.size()) {
      return (this.upper.getRoot() + this.lower.getRoot()) / 2;
    } else if (this.upper.size() > this.lower.size()) {
      return this.upper.getRoot();
    } else {
      return this.lower.getRoot();
    }
  }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */

class MinHeap {
  private heap: number[] = [];

  size(): number {
    return this.heap.length;
  }

  getRoot(): number {
    return this.heap[0];
  }

  insert(num: number): void {
    this.heap.push(num);
    this.bubbleUp();
  }

  removeRoot(): number {
    const top = this.heap[0];
    const end = this.heap.pop()!;

    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.bubbleDown();
    }

    return top;
  }

  // Fix after removal (downward)
  bubbleDown(): void {
    let idx = 0;
    const length = this.heap.length;
    const val = this.heap[0];

    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let swap = idx;

      if (leftIdx < length && this.heap[leftIdx] < this.heap[swap]) {
        swap = leftIdx;
      }

      if (rightIdx < length && this.heap[rightIdx] < this.heap[swap]) {
        swap = rightIdx;
      }

      if (swap === idx) break;

      this.heap[idx] = this.heap[swap];
      this.heap[swap] = val;
      idx = swap;
    }
  }

  // Fix after insert (upward)
  bubbleUp(): void {
    let idx = this.heap.length - 1;
    const val = this.heap[idx];
    // Heap as an array
    // left child: 2 * i + 1
    // right child: 2 * i + 2
    // parent: Math.floor((i-1) / 2)

    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      const parent = this.heap[parentIdx];

      if (val >= parent) break;

      this.heap[parentIdx] = val;
      this.heap[idx] = parent;
      idx = parentIdx;
    }
  }
}

class MaxHeap {
  private heap: number[] = [];

  size(): number {
    return this.heap.length;
  }

  getRoot(): number {
    return this.heap[0];
  }

  insert(num: number): void {
    this.heap.push(num);
    this.bubbleUp();
  }

  removeRoot(): number {
    const top = this.heap[0];
    const end = this.heap.pop()!;

    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.bubbleDown();
    }

    return top;
  }

  bubbleDown(): void {
    let idx = 0;
    const length = this.heap.length;
    const val = this.heap[0];

    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let swap = idx;

      if (leftIdx < length && this.heap[leftIdx] > this.heap[swap]) {
        swap = leftIdx;
      }

      if (rightIdx < length && this.heap[rightIdx] > this.heap[swap]) {
        swap = rightIdx;
      }

      if (swap === idx) break;

      this.heap[idx] = this.heap[swap];
      this.heap[swap] = val;
      idx = swap;
    }
  }

  bubbleUp(): void {
    let idx = this.heap.length - 1;
    const val = this.heap[idx];

    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      const parent = this.heap[parentIdx];

      if (val <= parent) break;

      this.heap[parentIdx] = val;
      this.heap[idx] = parent;
      idx = parentIdx;
    }
  }
}
