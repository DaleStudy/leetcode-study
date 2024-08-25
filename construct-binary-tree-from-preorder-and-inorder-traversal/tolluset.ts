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
 *  TC: O(n^2)
 *  SC: O(n)
 * */
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  if (!preorder?.length || !inorder?.length) {
    return null;
  }

  const rootValue = preorder[0];
  const root = new TreeNode(rootValue);
  const inorderRootIndex = inorder.indexOf(rootValue);

  root.left = buildTree(
    preorder.slice(1, inorderRootIndex + 1),
    inorder.slice(0, inorderRootIndex),
  );

  root.right = buildTree(
    preorder.slice(inorderRootIndex + 1),
    inorder.slice(inorderRootIndex + 1),
  );

  return root;
}
