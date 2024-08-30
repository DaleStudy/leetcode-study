/**
 * @description
 * brainstorming:
 * 1. asc sort + division calculate
 * 2. bfs + memoization
 *
 * strategy:
 * bfs + memoization
 *
 * reason:
 * Tried with brainstorming 1 but test case is false
 *
 * time complexity: O(n^k)
 * space complexity: O(n)
 */
class Node {
  constructor(val) {
    this.value = val;
    this.next = null;
  }
}

class CustomQueue {
  constructor() {
    this.front = null;
    this.rear = null;
    this.size = 0;
  }

  push(val) {
    const node = new Node(val);

    if (this.size === 0) {
      this.front = node;
      this.rear = node;
    } else {
      this.rear.next = node;
      this.rear = node;
    }

    this.size++;
  }

  pop() {
    if (this.size === 0) return null;
    const node = this.front;
    this.front = this.front.next;
    this.size--;
    if (this.size === 0) this.rear = null;

    return node.value;
  }
}

var coinChange = function (coins, amount) {
  const queue = new CustomQueue();
  const memoSet = new Set();

  if (amount === 0) return 0;

  for (const coin of coins) {
    if (amount === coin) return 1;

    queue.push(coin);
    memoSet.add(coin);
  }

  let count = 1;

  while (queue.size) {
    count++;
    let depthSize = queue.size;

    while (depthSize--) {
      const sum = queue.pop();

      for (const coin of coins) {
        const nextSum = sum + coin;

        if (memoSet.has(nextSum)) continue;
        if (amount === nextSum) return count;
        if (amount > nextSum) queue.push(nextSum);

        memoSet.add(nextSum);
      }
    }
  }

  return -1;
};
