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

// TC: O(m + n), m = number of nodes in root, n = number of nodes in subRoot
// SC: O(m + n)
function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  const serializeNode = (node: TreeNode | null) => {
    if (!node) return "$";

    const str = `(${node.val},${serializeNode(node.left)},${serializeNode(
      node.right
    )})`;

    return str;
  };

  const serializedRoot = serializeNode(root);
  const serializedSubRoot = serializeNode(subRoot);

  return serializedRoot.includes(serializedSubRoot);
}
