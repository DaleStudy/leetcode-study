// Time complexity: O(logn)
// Space complexity: O(logn)

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  // 1. 각자 부모 리스트 완성
  const search = (target, parent) => {
    const dfs = (current) => {
      if (target.val > current.val) {
        dfs(current.right);
      }

      if (target.val < current.val) {
        dfs(current.left);
      }

      parent.push(current);
    };

    dfs(root);
  };

  const parentP = [];
  const parentQ = [];

  search(p, parentP);
  search(q, parentQ);

  // 2. 공통 부모 탐색
  let answer = null;

  while (
    parentP.at(-1) &&
    parentQ.at(-1) &&
    parentP.at(-1).val === parentQ.at(-1).val
  ) {
    answer = parentP.at(-1);
    parentP.pop();
    parentQ.pop();
  }

  return answer;
};
