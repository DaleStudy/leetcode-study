// n: number of nodes
// Time complexity: O(n)
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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  const answer = [];
  const q = new _Queue();

  if (root) {
    q.push([root, 0]);
  }

  while (!q.isEmpty()) {
    const [current, lv] = q.shift();

    if (answer.at(lv) === undefined) {
      answer[lv] = [];
    }

    answer[lv].push(current.val);

    if (current.left) {
      q.push([current.left, lv + 1]);
    }

    if (current.right) {
      q.push([current.right, lv + 1]);
    }
  }

  return answer;
};
