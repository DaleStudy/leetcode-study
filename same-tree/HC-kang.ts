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

/**
 * https://leetcode.com/problems/same-tree/description/
 * T.C. O(n)
 * S.C. O(n)
 */
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  if (p === null && q === null) return true;
  if (p === null || q === null) return false;
  if (p.val !== q.val) return false;
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

/**
 * T.C. O(n)
 * S.C. O(n)
 */
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  const stack: [TreeNode | null, TreeNode | null][] = [[p, q]];

  while (stack.length) {
    const [node1, node2] = stack.pop()!;
    if (node1 === null && node2 === null) continue;
    if (node1 === null || node2 === null) return false;
    if (node1.val !== node2.val) return false;
    stack.push([node1.left, node2.left]);
    stack.push([node1.right, node2.right]);
  }

  return true;
}
