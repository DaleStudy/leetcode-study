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

/*
 * TC: O(n)
 * SC: O(n)
 * */
function kthSmallest(root: TreeNode, k: number): number {
  let count = 0;
  let result: null | number = null;

  const inOrder = (node: TreeNode | null) => {
    if (!node || result !== null) {
      return false;
    }

    if (inOrder(node.left)) {
      return true;
    }

    count++;

    if (count === k) {
      result = node.val;
      return true;
    }

    inOrder(node.right);
  };

  inOrder(root);

  return result!;
}
