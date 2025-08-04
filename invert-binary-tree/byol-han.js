/**
 * https://leetcode.com/problems/invert-binary-tree/submissions/1651537941/
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
  if (root === null) return null;

  // 왼쪽과 오른쪽 자식 노드 바꾸기
  [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];

  return root;
};
