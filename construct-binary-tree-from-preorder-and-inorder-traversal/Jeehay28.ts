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
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  const indices = {};
  //     indices = {
  //   9: 0,
  //   3: 1,
  //   15: 2,
  //   20: 3,
  //   7: 4
  // }

  for (let i = 0; i < inorder.length; i++) {
    const num = inorder[i];
    indices[num] = i;
  }

  let preIndex = 0;

  const dfs = (start: number, end: number) => {
    if (start > end) return null;
    const val = preorder[preIndex];
    preIndex++;
    const mid = indices[val];

    const left = dfs(start, mid - 1);
    const right = dfs(mid + 1, end);

    return new TreeNode(val, left, right);
  };

  return dfs(0, inorder.length - 1);
}
