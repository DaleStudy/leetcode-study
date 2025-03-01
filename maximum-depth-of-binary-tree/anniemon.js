/**
 * 시간 복잡도:
 *   노드의 갯수만큼 탐색하므로, O(n)
 * 공간 복잡도:
 *   재귀 호출 스택의 크기는 트리가 한쪽으로 치우친 경우 O(n)로 최악이 되고,
 *   균형 잡힌 트리의 경우 O(log n)이다.
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
var maxDepth = function(root) {
  const dfs = (node) => {
      if(!node) return 0;
      return Math.max(dfs(node.left) + 1, dfs(node.right) + 1);
  }
  return dfs(root);
};
