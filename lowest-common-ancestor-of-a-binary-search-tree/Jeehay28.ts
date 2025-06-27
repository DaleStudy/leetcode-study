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

// TC: O(n)
// SC: O(1)
function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null {
  if (!root || !p || !q) return null;

  let node = root;

  while (node) {
    if (node.val < p.val && node.val < q.val) {
      node = node.right!;
    } else if (node.val > p.val && node.val > q.val) {
      node = node.left!;
    } else {
      return node;
    }
  }

  return null;
}


// TC: O(n)
// SC: O(n)
// function lowestCommonAncestor(
//   root: TreeNode | null,
//   p: TreeNode | null,
//   q: TreeNode | null
// ): TreeNode | null {
//   if (!root || !p || !q) return null;

//   if (p.val < root.val && q.val < root.val) {
//     return lowestCommonAncestor(root.left, p, q);
//   } else if (p.val > root.val && q.val > root.val) {
//     return lowestCommonAncestor(root.right, p, q);
//   } else {
//     return root;
//   }
// }
