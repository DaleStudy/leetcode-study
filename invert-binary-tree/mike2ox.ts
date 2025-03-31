/**
 * Source: https://leetcode.com/problems/invert-binary-tree/
 * 풀이방법: 재귀를 이용하여 트리를 뒤집음
 *
 * 시간복잡도: O(n) - n은 트리의 노드 수
 * 공간복잡도: O(n) - 재귀 호출에 따른 스택 메모리
 *
 * 다른 풀이방법
 * - BFS를 이용하여 풀이
 * - 스택을 이용하여 풀이
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

function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return null;

  const result = new TreeNode(
    root.val,
    invertTree(root.right),
    invertTree(root.left)
  );
  return result;
}
