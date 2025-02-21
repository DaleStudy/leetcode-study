/**
 * Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
 * 접근법: 최대 깊이만 고려하면 되기에 탐색 알고리즘 중 하나 선택
 *
 * 시간복잡도: O(N) - 편향 트리인 경우, 모든 노드(N개) 검색
 * 공간복잡도: O(H) - 트리높이
 *
 * 다른 접근법
 * - 재귀를 통해 가독성있는 코드 작성 가능(But, 깊이가 커지면 스택오버플로우가
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

// solution1: array를 stack처럼 사용하면서 DFS구현
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;
  const stack = new Array({ node: root, depth: 1 });
  let maxDepth = 1;
  while (stack.length) {
    const now = stack.pop();
    if (!now.node?.left && !now.node?.right) {
      if (now.depth > maxDepth) maxDepth = now.depth;
      continue;
    }
    stack.push({ node: now.node.left, depth: now.depth + 1 });
    stack.push({ node: now.node.right, depth: now.depth + 1 });
  }
  return maxDepth;
}

// solution2: recursion으로 DFS구현
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;
  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
}
