/**
 * https://leetcode.com/problems/find-median-from-data-stream
 * array with binary search
 */
class MedianFinder {
  // S.C. O(n)
  private nums: number[] = [];

  // T.C. O(n)
  addNum(num: number): void {
    if (this.nums.length === 0) {
      this.nums.push(num);
      return;
    } else {
      this.putNumWithBinarySearch(num);
    }
  }

  private putNumWithBinarySearch(num: number): void {
    let left = 0;
    let right = this.nums.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (this.nums[mid] === num) {
        this.nums.splice(mid, 0, num);
        return;
      } else if (this.nums[mid] < num) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    // T.C. O(n)
    this.nums.splice(left, 0, num);
  }

  // T.C. O(1)
  findMedian(): number {
    const len = this.nums.length;

    if (len % 2 === 1) {
      return this.nums[Math.floor(len / 2)];
    } else {
      return (this.nums[len / 2] + this.nums[len / 2 - 1]) / 2;
    }
  }
}

/**
 * heap...
 * TL;DR
 */
class MedianFinder {
  // S.C. O(n)
  private smallHalf: MaxHeap = new MaxHeap();
  private largeHalf: MinHeap = new MinHeap();

  // T.C. O(log n)
  addNum(num: number): void {
    this.smallHalf.push(num);
    this.largeHalf.push(this.smallHalf.pop()!);

    if (this.smallHalf.size() < this.largeHalf.size()) {
      this.smallHalf.push(this.largeHalf.pop()!);
    }
  }

  // T.C. O(1)
  findMedian(): number {
    if (this.smallHalf.size() === this.largeHalf.size()) {
      return (this.smallHalf.peek()! + this.largeHalf.peek()!) / 2;
    } else {
      return this.smallHalf.peek()!;
    }
  }
}

class MinHeap {
  protected heap: number[] = [];

  push(val: number): void {
    this.heap.push(val);
    this.heapifyUp();
  }

  pop(): number | undefined {
    if (this.heap.length === 0) return undefined;
    if (this.heap.length === 1) return this.heap.pop();

    const result = this.heap[0];
    this.heap[0] = this.heap.pop()!;
    this.heapifyDown();
    return result;
  }

  peek(): number | undefined {
    return this.heap[0];
  }

  size(): number {
    return this.heap.length;
  }

  private heapifyUp(): void {
    let index = this.heap.length - 1;
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[parentIndex] <= this.heap[index]) break;

      this.swap(parentIndex, index);
      index = parentIndex;
    }
  }

  private heapifyDown(): void {
    let index = 0;
    while (true) {
      let smallest = index;
      const leftChild = 2 * index + 1;
      const rightChild = 2 * index + 2;

      if (
        leftChild < this.heap.length &&
        this.heap[leftChild] < this.heap[smallest]
      ) {
        smallest = leftChild;
      }

      if (
        rightChild < this.heap.length &&
        this.heap[rightChild] < this.heap[smallest]
      ) {
        smallest = rightChild;
      }

      if (smallest === index) break;

      this.swap(index, smallest);
      index = smallest;
    }
  }

  protected swap(i: number, j: number): void {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
}

class MaxHeap extends MinHeap {
  push(val: number): void {
    super.push(-val);
  }

  pop(): number | undefined {
    const val = super.pop();
    return val === undefined ? undefined : -val;
  }

  peek(): number | undefined {
    const val = super.peek();
    return val === undefined ? undefined : -val;
  }
}
