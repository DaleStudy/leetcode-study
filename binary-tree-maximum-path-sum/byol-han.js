/**
 * https://leetcode.com/problems/binary-tree-maximum-path-sum/
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
var maxPathSum = function (root) {
  let maxSum = -Infinity; // global max

  function dfs(node) {
    if (!node) return 0;

    // 왼쪽과 오른쪽 서브트리에서 최대 경로 합을 구한다
    // 음수면 0으로 치환 (해당 서브트리를 포함하지 않는게 더 이득인 경우)
    let leftMax = Math.max(0, dfs(node.left));
    let rightMax = Math.max(0, dfs(node.right));

    // 현재 노드를 루트로 하는 경로에서 최대값을 계산 (left + node + right)
    let currentMax = leftMax + node.val + rightMax;

    // global 최대값 갱신
    maxSum = Math.max(maxSum, currentMax);

    // 부모 노드로 return 시: 한쪽 방향으로만 선택 가능
    return node.val + Math.max(leftMax, rightMax);
  }

  dfs(root);
  return maxSum;
};
