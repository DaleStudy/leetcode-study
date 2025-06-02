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
// SC: O(n)
function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return null;

  const left = invertTree(root.right);
  const right = invertTree(root.left);

  root.left = left;
  root.right = right;

  return root;
}


// TC: O(n)
// SC: O(n)
// function invertTree(root: TreeNode | null): TreeNode | null {
//     if (!root) return null;

//     [root.left, root.right] = [root.right, root.left];

//     invertTree(root.left);
//     invertTree(root.right);

//     return root;

// }


// TC: O(n)
// SC: O(n)
// function invertTree(root: TreeNode | null): TreeNode | null {
//   if (!root) return null;

//   const stack: (TreeNode | null)[] = [root];

//   while (stack.length > 0) {
//     const node = stack.pop();

//     if (!node) continue;

//     [node.left, node.right] = [node.right, node.left];

//     stack.push(node.left);
//     stack.push(node.right);
//   }

//   return root;
// }

