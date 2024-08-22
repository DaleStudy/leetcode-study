// Definition for a binary tree node.
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

// T.C: O(N)
// S.C: O(N)
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  if (preorder.length === 0 || inorder.length === 0) {
    return null;
  }
  const root = new TreeNode(preorder[0]);
  const idx = inorder.indexOf(preorder[0]);
  root.left = buildTree(preorder.slice(1, idx + 1), inorder.slice(0, idx));
  root.right = buildTree(preorder.slice(idx + 1), inorder.slice(idx + 1));

  return root;
}

// Not using slice. but I think it's not necessary... first solution is more readable. and that's not so bad.
// T.C: O(N)
// S.C: O(N)
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  // this tree is consist of unique values
  const inorderMap = new Map<number, number>();
  for (const [i, val] of inorder.entries()) {
    inorderMap.set(val, i);
  }

  function helper(preLeft: number, preRight: number, inLeft: number, inRight: number): TreeNode | null {
    if (preLeft > preRight) return null;

    const rootValue = preorder[preLeft];
    const root = new TreeNode(rootValue);
    const inRootIdx = inorderMap.get(rootValue)!;

    const leftSize = inRootIdx - inLeft;

    root.left = helper(preLeft + 1, preLeft + leftSize, inLeft, inRootIdx - 1);
    root.right = helper(preLeft + leftSize + 1, preRight, inRootIdx + 1, inRight);

    return root;
  }

  return helper(0, preorder.length - 1, 0, inorder.length - 1);
}