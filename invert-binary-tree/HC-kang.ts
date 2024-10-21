// class TreeNode {
//   val: number;
//   left: TreeNode | null;
//   right: TreeNode | null;
//   constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//     this.val = val === undefined ? 0 : val;
//     this.left = left === undefined ? null : left;
//     this.right = right === undefined ? null : right;
//   }
// }

/**
 * https://leetcode.com/problems/invert-binary-tree
 * T.C. O(n)
 * S.C. O(n)
 */
function invertTree(root: TreeNode | null): TreeNode | null {
  if (root === null) {
    return null;
  }

  [root.left, root.right] = [root.right, root.left];
  invertTree(root.left);
  invertTree(root.right);

  return root;
}

/**
 * T.C. O(n)
 * S.C. O(n)
 */
function invertTree(root: TreeNode | null): TreeNode | null {
  const stack: Array<TreeNode | null> = [root];

  while (stack.length > 0) {
    const node = stack.pop()!;

    if (node === null) {
      continue;
    }

    [node.left, node.right] = [node.right, node.left];
    stack.push(node.left, node.right);
  }

  return root;
}
