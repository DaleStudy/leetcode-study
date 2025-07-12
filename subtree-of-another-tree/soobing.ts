/**
 * 문제 설명
 * - 두 개의 이진트리 중, subTree가 존재하는지 확인하는 문제
 *
 * 아이디어
 * 1) DFS + isSameTree 체크
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

function isSameTree(tree1: TreeNode | null, tree2: TreeNode | null) {
  if ((tree1 && !tree2) || (!tree1 && tree2)) return false;
  if (tree1 === null && tree2 === null) return true;
  if (tree1?.val !== tree2?.val) return false;
  return (
    isSameTree(tree1?.left ?? null, tree2?.left ?? null) &&
    isSameTree(tree1?.right ?? null, tree2?.right ?? null)
  );
}

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  if (!root) return false;
  if (isSameTree(root, subRoot)) return true;
  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
}
