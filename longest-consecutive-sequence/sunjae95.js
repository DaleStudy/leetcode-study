/**
 * @description
 * brainstorming:
 * priority queue + result counting that priority queue was pop
 *
 * time complexity: O(n log n)
 * space complexity: O(n)
 */
var longestConsecutive = function (nums) {
  const queue = new CustomQueue();
  let [count, before, answer] = [0, null, 0];

  nums.forEach((n) => queue.insert(n));

  if (queue.size === 0) return count;

  [count, before, answer] = [1, queue.remove(), 1];

  while (queue.size) {
    const current = queue.remove();

    if (before === current) continue;

    count = before + 1 === current ? count + 1 : 1;
    before = current;
    answer = Math.max(answer, count);
  }

  return answer;
};

class Node {
  constructor(value) {
    this.value = value;
  }
}

class CustomQueue {
  constructor() {
    this.items = new Map();
    this.size = 0;
  }

  parentIndex(index) {
    return Math.floor((index - 1) / 2);
  }

  leftChildIndex(index) {
    return 2 * index + 1;
  }

  rightChildIndex(index) {
    return 2 * index + 2;
  }

  heapifyUp() {
    let index = this.size - 1;

    while (index > 0) {
      const parentIndex = this.parentIndex(index);
      const parent = this.items.get(parentIndex);
      const current = this.items.get(index);

      if (parent.value <= current.value) break;

      this.items.set(this.parentIndex(index), current);
      this.items.set(index, parent);

      index = parentIndex;
    }
  }

  heapifyDown() {
    let index = 0;

    while (this.leftChildIndex(index) < this.items.size) {
      let smallestIndex = this.leftChildIndex(index);
      let rightIndex = this.rightChildIndex(index);
      const current = this.items.get(index);

      if (
        rightIndex < this.size &&
        this.items.get(rightIndex).value < this.items.get(smallestIndex).value
      ) {
        smallestIndex = rightIndex;
      }

      if (current.value <= this.items.get(smallestIndex).value) break;
      this.items.set(index, this.items.get(smallestIndex));
      this.items.set(smallestIndex, current);
      index = smallestIndex;
    }
  }

  insert(value) {
    const index = this.size;
    const node = new Node(value);
    this.items.set(index, node);
    this.size++;
    this.heapifyUp();
  }

  remove() {
    if (this.size === 0) return null;

    const root = this.items.get(0);
    this.items.set(0, this.items.get(this.size - 1));
    this.items.delete(this.size - 1);
    this.size--;

    this.heapifyDown();
    return root.value;
  }
}
