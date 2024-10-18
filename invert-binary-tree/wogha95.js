/**
 * 양쪽 자식 노드 주소를 교환하고 dfs로 순회합니다.
 *
 * TC: O(N)
 * 모든 트리를 순회합니다.
 *
 * SC: O(N)
 * 최악의 경우 (한쪽으로 치우친 트리) N만큼 CallStack이 생깁니다.
 *
 * N: tree의 모든 node 수
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
 * @return {TreeNode}
 */
var invertTree = function (root) {
  if (!root) {
    return root;
  }
  [root.left, root.right] = [root.right, root.left];
  invertTree(root.left);
  invertTree(root.right);
  return root;
};
