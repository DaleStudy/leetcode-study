/**
 * Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
 * Solution: DFS를 이용해서 두 노드까지의 경로를 구해 순차적으로 비교하면서 가장 마지막 동일 노드를 추출
 *
 * 시간복잡도: O(N) - 최악인 경우, 전체 노드수 탐색
 * 공간복잡도: O(N) - 최악인 경우, 전체 노드수 보관
 *
 * 다른 풀이
 * - 재귀로도 해결할 것으로 보이지만 바로 구현체가 떠오르지 않음
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

function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null {
  if (!root || !p || !q) return null;
  let stack = new Array(root);
  let pRoute: Array<TreeNode> | null;
  let qRoute: Array<TreeNode> | null;
  let answer: TreeNode | null;
  const visited = new Set();

  while (stack.length) {
    const left = stack.at(-1).left;
    if (left && !visited.has(left.val)) {
      stack.push(left);
      continue;
    }
    const right = stack.at(-1).right;
    if (right && !visited.has(right.val)) {
      stack.push(right);
      continue;
    }
    const now = stack.pop();
    visited.add(now.val);
    if (now.val === q.val) {
      qRoute = [...stack, now];
      continue;
    }
    if (now.val === p.val) {
      pRoute = [...stack, now];
      continue;
    }
  }
  const shortLength =
    pRoute.length > qRoute.length ? qRoute.length : pRoute.length;
  for (let i = 0; i < shortLength; i++) {
    if (pRoute.at(i) !== qRoute.at(i)) {
      answer = pRoute.at(i - 1);
      break;
    }
  }
  return answer ? answer : pRoute.at(shortLength - 1);
}
