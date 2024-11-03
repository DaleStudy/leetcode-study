/**
 * TC: O(N)
 * SC: O(N)
 * N: count of node in tree
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
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  const queueP = [p];
  const queueQ = [q];

  while (queueP.length > 0 && queueQ.length > 0) {
    const currentP = queueP.shift();
    const currentQ = queueQ.shift();

    if (currentP === null && currentQ === null) {
      continue;
    }

    if (currentP === null || currentQ === null) {
      return false;
    }

    if (currentP.val !== currentQ.val) {
      return false;
    }

    queueP.push(currentP.left);
    queueP.push(currentP.right);

    queueQ.push(currentQ.left);
    queueQ.push(currentQ.right);
  }

  return queueP.length === 0 && queueQ.length === 0;
};
