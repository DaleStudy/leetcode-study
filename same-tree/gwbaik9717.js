// n: number of nodes
// Time complexity: O(n)
// Space complexity: O(n)

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
  const dfs = (currentP, currentQ) => {
    if (currentP.val !== currentQ.val) {
      return false;
    }

    if (
      (currentP.left && !currentQ.left) ||
      (!currentP.left && currentQ.left)
    ) {
      return false;
    }

    if (
      (currentP.right && !currentQ.right) ||
      (!currentP.right && currentQ.right)
    ) {
      return false;
    }

    if (currentP.left && currentQ.left) {
      if (!dfs(currentP.left, currentQ.left)) {
        return false;
      }
    }

    if (currentP.right && currentQ.right) {
      if (!dfs(currentP.right, currentQ.right)) {
        return false;
      }
    }

    return true;
  };

  if ((p && !q) || (!p && q)) {
    return false;
  }

  if (p && q) {
    return dfs(p, q);
  }

  return true;
};
