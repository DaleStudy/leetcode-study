// n: number of nodes, h: height of tree (max: n)
// Time complexity: O(n)
// Space complexity: O(2^h)

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

class _Queue {
  constructor() {
    this.q = [];
    this.left = 0;
    this.right = 0;
  }

  push(value) {
    this.q.push(value);
    this.right++;
  }

  shift() {
    const rv = this.q[this.left];
    delete this.q[this.left++];

    return rv;
  }

  isEmpty() {
    return this.left === this.right;
  }
}

const isValid = (data) => {
  if (data === undefined || data === null) {
    return false;
  }

  return true;
};

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function (root) {
  const answer = [null];

  const bfs = (current) => {
    const q = new _Queue();
    q.push([1, current]);

    while (!q.isEmpty()) {
      const [i, current] = q.shift();

      if (current === null) {
        answer[i] = current;
        continue;
      }

      answer[i] = current.val;

      const left = 2 * i;
      const right = left + 1;

      if (current.left) {
        q.push([left, current.left]);
      } else {
        q.push([left, null]);
      }

      if (current.right) {
        q.push([right, current.right]);
      } else {
        q.push([right, null]);
      }
    }
  };

  bfs(root);

  while (answer.length > 1 && !isValid(answer.at(-1))) {
    answer.pop();
  }

  return answer;
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function (data) {
  if (data.length === 1) {
    return null;
  }

  const root = new TreeNode(data[1]);
  const q = new _Queue();
  q.push([1, root]);

  while (!q.isEmpty()) {
    const [i, current] = q.shift();

    const left = i * 2;
    const right = left + 1;

    if (left <= data.length && isValid(data[left])) {
      current.left = new TreeNode(data[left]);
      q.push([left, current.left]);
    }

    if (right <= data.length && isValid(data[right])) {
      current.right = new TreeNode(data[right]);
      q.push([right, current.right]);
    }
  }

  return root;
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
