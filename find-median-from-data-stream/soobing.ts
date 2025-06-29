/**
 * 문제 설명
 * - 중간 값을 찾는 문제
 *
 * 아이디어 (👀 어려움..)
 * - 최대 힙과 최소 힙을 사용하여 중간 값을 찾는다.
 */
class MinHeap {
  heap: number[] = [];
  size(): number {
    return this.heap.length;
  }
  peek(): number | null {
    return this.heap[0] ?? null;
  }
  push(val: number) {
    this.heap.push(val);
    this.bubbleUp(this.size() - 1);
  }
  pop(): number | null {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const end = this.heap.pop()!;
    if (this.size() > 0) {
      this.heap[0] = end;
      this.bubbleDown(0);
    }
    return top;
  }
  private bubbleUp(idx: number) {
    while (idx > 0) {
      const parent = Math.floor((idx - 1) / 2);
      if (this.heap[parent] <= this.heap[idx]) break;
      [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
      idx = parent;
    }
  }
  private bubbleDown(idx: number) {
    const n = this.size();
    while (true) {
      let left = idx * 2 + 1;
      let right = idx * 2 + 2;
      let smallest = idx;
      if (left < n && this.heap[left] < this.heap[smallest]) smallest = left;
      if (right < n && this.heap[right] < this.heap[smallest]) smallest = right;
      if (smallest === idx) break;
      [this.heap[smallest], this.heap[idx]] = [
        this.heap[idx],
        this.heap[smallest],
      ];
      idx = smallest;
    }
  }
}

class MaxHeap {
  heap: number[] = [];
  size(): number {
    return this.heap.length;
  }
  peek(): number | null {
    return this.heap[0] ?? null;
  }
  push(val: number) {
    this.heap.push(val);
    this.bubbleUp(this.size() - 1);
  }
  pop(): number | null {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const end = this.heap.pop()!;
    if (this.size() > 0) {
      this.heap[0] = end;
      this.bubbleDown(0);
    }
    return top;
  }
  private bubbleUp(idx: number) {
    while (idx > 0) {
      const parent = Math.floor((idx - 1) / 2);
      if (this.heap[parent] >= this.heap[idx]) break;
      [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
      idx = parent;
    }
  }
  private bubbleDown(idx: number) {
    const n = this.size();
    while (true) {
      let left = idx * 2 + 1;
      let right = idx * 2 + 2;
      let largest = idx;
      if (left < n && this.heap[left] > this.heap[largest]) largest = left;
      if (right < n && this.heap[right] > this.heap[largest]) largest = right;
      if (largest === idx) break;
      [this.heap[largest], this.heap[idx]] = [
        this.heap[idx],
        this.heap[largest],
      ];
      idx = largest;
    }
  }
}

class MedianFinder {
  private minH = new MinHeap();
  private maxH = new MaxHeap();

  addNum(num: number): void {
    if (this.maxH.size() === 0 || num <= (this.maxH.peek() ?? num)) {
      this.maxH.push(num);
    } else {
      this.minH.push(num);
    }

    // Rebalance
    if (this.maxH.size() > this.minH.size() + 1) {
      this.minH.push(this.maxH.pop()!);
    } else if (this.minH.size() > this.maxH.size()) {
      this.maxH.push(this.minH.pop()!);
    }
  }

  findMedian(): number {
    const total = this.maxH.size() + this.minH.size();
    if (total % 2 === 1) {
      return this.maxH.peek()!;
    } else {
      return (this.maxH.peek()! + this.minH.peek()!) / 2;
    }
  }
}
