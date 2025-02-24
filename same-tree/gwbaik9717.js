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
    if (!currentP && !currentQ) {
      return true;
    }

    if ((!currentP && currentQ) || (currentP && !currentQ)) {
      return false;
    }

    if (currentP.val !== currentQ.val) {
      return false;
    }

    return (
      dfs(currentP.left, currentQ.left) && dfs(currentP.right, currentQ.right)
    );
  };

  return dfs(p, q);
};
