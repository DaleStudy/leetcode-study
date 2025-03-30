// n: number of nodes in root, m: number of nodes in subroot
// Time complexity: O(n*m)
// Space complexity: O(n)

class _Queue {
  constructor() {
    this.q = [];
    this.front = 0;
    this.rear = 0;
  }

  isEmpty() {
    return this.front === this.rear;
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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  const check = (root, subRoot) => {
    const q = new _Queue();
    q.push([root, subRoot]);

    while (!q.isEmpty()) {
      const [node, subNode] = q.shift();

      if (node.val !== subNode.val) {
        return false;
      }

      if ((node.left && !subNode.left) || (!node.left && subNode.left)) {
        return false;
      }

      if ((node.right && !subNode.right) || (!node.right && subNode.right)) {
        return false;
      }

      if (node.left && subNode.left) {
        q.push([node.left, subNode.left]);
      }

      if (node.right && subNode.right) {
        q.push([node.right, subNode.right]);
      }
    }

    return true;
  };

  const q = new _Queue();
  q.push(root);

  while (!q.isEmpty()) {
    const current = q.shift();

    if (check(current, subRoot)) {
      return true;
    }

    if (current.left) {
      q.push(current.left);
    }

    if (current.right) {
      q.push(current.right);
    }
  }

  return false;
};
