/**
 * 문제 설명
 * - 이진 트리를 반전시키는 문제
 *
 * 아이디어
 * 1) DFS / BFS 로 탐색하면서 반전시키기
 * - 시간 복잡도 O(n): 모든 노드 한번씩 방문
 * - 공간 복잡도 DFS의 경우 O(h), BFS의 경우 O(2/n) -> 마지막 레벨의 노드 수
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

function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return null;

  const left = invertTree(root.left);
  const right = invertTree(root.right);

  root.left = right;
  root.right = left;

  return root;
}

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

function invertTreeBFS(root: TreeNode | null): TreeNode | null {
  const queue: (TreeNode | null)[] = [root];

  while (queue.length > 0) {
    const current = queue.shift();
    if (current) {
      const left = current.left;
      const right = current.right;
      current.left = right;
      current.right = left;

      queue.push(left);
      queue.push(right);
    }
  }
  return root;
}
