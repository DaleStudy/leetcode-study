/**
 * Source: https://leetcode.com/problems/same-tree/
 * Solution: 트리의 노드를 순회하면서 값이 같은지 확인
 * 시간 복잡도: O(N) - 트리의 모든 노드를 한번씩 방문
 * 공간 복잡도: O(N) - 스택에 최대 트리의 높이만큼 쌓일 수 있음
 *
 * 추가 사항
 * - 트리를 순회만 하면 되기에 Typescript로 Stack을 활용해 DFS로 해결
 * - 재귀로 구현하면 간단하게 구현 가능
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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  if (!q || !p) return !q === !p;
  let result = true;
  let stack = new Array({
    left: p,
    right: q,
  });
  while (stack.length) {
    const now = stack.pop();
    const left = now?.left;
    const right = now?.right;
    const isLeafNode =
      !left?.left && !left?.right && !right?.right && !right?.left;
    const isSameValue = left?.val === right?.val;
    const hasDifferentSubtree =
      (!left?.left && right?.left) || (!left?.right && right?.right);
    if (isLeafNode && isSameValue) continue;
    if (!isSameValue || hasDifferentSubtree) {
      result = false;
      break;
    }
    stack.push({ left: left?.left, right: right?.left });
    stack.push({ left: left?.right, right: right?.right });
  }
  return result;
}

// Solution 2 - 재귀
function isSameTree2(p: TreeNode | null, q: TreeNode | null): boolean {
  if (!p && !q) return true;
  if (!p || !q) return false;
  if (p.val !== q.val) return false;

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
