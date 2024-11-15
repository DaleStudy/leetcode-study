/**
 * 1차
 *
 * TC: O(N)
 * SC: O(N)
 * N: total of nodes
 */

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
  const result = [];

  const queue = [
    {
      level: 0,
      current: root,
    },
  ];

  while (queue.length > 0) {
    const { level, current } = queue.shift();

    if (!current) {
      continue;
    }

    if (result[level]) {
      result[level].push(current.val);
    } else {
      result[level] = [current.val];
    }

    if (current.left) {
      queue.push({
        level: level + 1,
        current: current.left,
      });
    }

    if (current.right) {
      queue.push({
        level: level + 1,
        current: current.right,
      });
    }
  }

  return result;
};
