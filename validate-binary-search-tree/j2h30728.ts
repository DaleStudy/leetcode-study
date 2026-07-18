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
 * 시간 복잡도 : O(n) - 모든 노드를 한 번씩 방문
 * 공간 복잡도 : O(h) - 재귀 호출 스택 깊이 (h는 트리 높이, 최악의 경우 O(n))
 */
function isValidBST(root: TreeNode | null): boolean {
  function validate(node: TreeNode | null, min: number, max: number): boolean {
    if (node === null) return true;

    if (node.val <= min || node.val >= max) return false;

    return (
      validate(node.left, min, node.val) && validate(node.right, node.val, max)
    );
  }
  return validate(root, -Infinity, Infinity);
}
