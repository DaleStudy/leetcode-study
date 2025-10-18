class MedianFinder {
  private left: PriorityQueue<number>;
  private right: PriorityQueue<number>;

  constructor() {
    this.left = new PriorityQueue<number>((a, b) => b - a); // 최대 힙
    this.right = new PriorityQueue<number>((a, b) => a - b); // 최소 힙
  }

  addNum(num: number): void {
    if (this.left.isEmpty() || num <= this.left.front()) {
      this.left.enqueue(num);
    } else {
      this.right.enqueue(num);
    }

    if (this.left.size() > this.right.size() + 1) {
      this.right.enqueue(this.left.dequeue());
    }

    if (this.right.size() > this.left.size()) {
      this.left.enqueue(this.right.dequeue());
    }

    if (!this.right.isEmpty() && this.left.front() > this.right.front()) {
      const maxValue = this.left.dequeue();

      this.right.enqueue(maxValue);
    }
  }

  findMedian(): number {
    let result = 0;

    if (this.left.size() === this.right.size()) {
      result = (this.left.front() + this.right.front()) / 2;
    } else if (this.left.size() === this.right.size() + 1) {
      result = this.left.front();
    }

    return result;
  }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
