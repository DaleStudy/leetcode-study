/**
 * 문제 설명
 * - 두 이진 트리가 같은지 확인하는 문제
 *
 * 아이디어
 * 1) 트리 탐색 (BFS, DFS)을 하면서 비교한다.
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

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  if (!p && !q) return true;
  if (!p || !q) return false;
  if (p.val !== q.val) return false;

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

function isSameTreeBFS(p: TreeNode | null, q: TreeNode | null): boolean {
  const queue1: (TreeNode | null)[] = [p];
  const queue2: (TreeNode | null)[] = [q];

  while (queue1.length > 0 && queue2.length > 0) {
    const node1 = queue1.shift();
    const node2 = queue2.shift();

    if (!node1 && !node2) continue;
    if (!node1 || !node2) return false;
    if (node1.val !== node2.val) return false;

    queue1.push(node1.left);
    queue1.push(node1.right);
    queue2.push(node2.left);
    queue2.push(node2.right);
  }

  return queue1.length === queue2.length;
}
