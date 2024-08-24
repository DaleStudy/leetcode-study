// TC: O(N) - leetcode analyze 기준
// SC: O(N)

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  if (inorder.length === 0) {
    return null;
  }

  const rootValue = preorder[0];
  const leftNodeLength = inorder.findIndex((value) => value === rootValue);
  const leftNode = buildTree(
    preorder.slice(1, 1 + leftNodeLength),
    inorder.slice(0, leftNodeLength)
  );
  const rightNode = buildTree(
    preorder.slice(1 + leftNodeLength),
    inorder.slice(leftNodeLength + 1)
  );
  return new TreeNode(rootValue, leftNode, rightNode);
};
