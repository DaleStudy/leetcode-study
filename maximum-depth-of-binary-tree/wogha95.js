/**
 * TC: O(N)
 * 모든 노드를 순회합니다.
 *
 * SC: O(N)
 * 노드의 수에 비례해서 queue의 길이가 증가됩니다.
 *
 * N: count of tree node
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
 * @return {number}
 */
var maxDepth = function (root) {
  let maximumDepth = 0;

  const queue = [[root, 1]];
  while (queue.length > 0) {
    const [current, depth] = queue.shift();

    if (current === null) {
      break;
    }

    maximumDepth = Math.max(maximumDepth, depth);

    if (current.left) {
      queue.push([current.left, depth + 1]);
    }

    if (current.right) {
      queue.push([current.right, depth + 1]);
    }
  }

  return maximumDepth;
};
