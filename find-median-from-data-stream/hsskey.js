class Heap {
    constructor(compare) {
      this.data = [];
      this.compare = compare;
    }
  
    size() {
      return this.data.length;
    }
  
    peek() {
      return this.data[0];
    }
  
    push(val) {
      this.data.push(val);
      this._siftUp();
    }
  
    pop() {
      const top = this.peek();
      const bottom = this.data.pop();
      if (this.data.length > 0) {
        this.data[0] = bottom;
        this._siftDown();
      }
      return top;
    }
  
    _siftUp() {
      let i = this.data.length - 1;
      const node = this.data[i];
      while (i > 0) {
        const parent = Math.floor((i - 1) / 2);
        if (this.compare(node, this.data[parent])) {
          this.data[i] = this.data[parent];
          i = parent;
        } else break;
      }
      this.data[i] = node;
    }
  
    _siftDown() {
      let i = 0;
      const node = this.data[0];
      const length = this.data.length;
  
      while (true) {
        let left = 2 * i + 1;
        let right = 2 * i + 2;
        let swap = i;
  
        if (left < length && this.compare(this.data[left], this.data[swap])) {
          swap = left;
        }
        if (right < length && this.compare(this.data[right], this.data[swap])) {
          swap = right;
        }
        if (swap === i) break;
  
        this.data[i] = this.data[swap];
        i = swap;
      }
  
      this.data[i] = node;
    }
  }
  
  var MedianFinder = function () {
    this.small = new Heap((a, b) => a > b); // max heap
    this.large = new Heap((a, b) => a < b); // min heap
  };
  
  MedianFinder.prototype.addNum = function (num) {
    this.small.push(num);
  
    if (
      this.small.size() > 0 &&
      this.large.size() > 0 &&
      this.small.peek() > this.large.peek()
    ) {
      this.large.push(this.small.pop());
    }
  
    if (this.small.size() > this.large.size() + 1) {
      this.large.push(this.small.pop());
    }
    if (this.large.size() > this.small.size() + 1) {
      this.small.push(this.large.pop());
    }
  };
  
  MedianFinder.prototype.findMedian = function () {
    if (this.small.size() > this.large.size()) {
      return this.small.peek();
    }
    if (this.large.size() > this.small.size()) {
      return this.large.peek();
    }
    return (this.small.peek() + this.large.peek()) / 2;
  };
  