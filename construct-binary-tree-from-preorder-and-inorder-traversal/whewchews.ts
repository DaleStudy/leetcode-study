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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  // build 함수가 각 노드마다 호출됨(N) * 각 노드마다 shift, indexOf 수행(N) = O(N^2)
  function build(preorder, inorder) {
    if (inorder.length) {
      // TC: O(N)
      const idx = inorder.indexOf(preorder.shift());
      const root = new TreeNode(inorder[idx]);

      root.left = build(preorder, inorder.slice(0, idx));
      root.right = build(preorder, inorder.slice(idx + 1));

      return root;
    }
    return null;
  }

  return build(preorder, inorder);
}

// TC: O(N^2)
// SC: O(N^2)
