/**
 * 문제 설명
 * - 주어진 이진 트리에서 최대 경로 합을 구하는 문제
 *
 * 아이디어
 * 1) 분할정복 + DFS
 *   - DFS 아이디어: 각 노드를 루트로 하는 서브트리에서, 해당 노드를 포함한 최대 경로 합을 구해 전역 변수 maxSum을 업데이트한다.
 *   - 현재 노드 기준의 최대 경로 합은: 현재 노드의 값 + 왼쪽 서브트리에서의 최대 경로 + 오른쪽 서브트리에서의 최대 경로.
 *   - 하지만 dfs 함수의 반환값은 부모 노드에 연결될 수 있는 일방향 경로이므로,
 *     '현재 노드의 값 + (왼쪽 또는 오른쪽 중 더 큰 값)'을 반환해야 한다.
 */

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function maxPathSum(root: TreeNode | null): number {
  let maxSum = -Infinity;

  function dfs(node: TreeNode | null) {
    if (!node) return 0;

    const leftMaxSum = Math.max(dfs(node.left), 0);
    const rightMaxSum = Math.max(dfs(node.right), 0);
    const current = leftMaxSum + rightMaxSum + node.val;
    maxSum = Math.max(current, maxSum);

    return node.val + Math.max(leftMaxSum, rightMaxSum);
  }

  dfs(root);

  return maxSum;
}
