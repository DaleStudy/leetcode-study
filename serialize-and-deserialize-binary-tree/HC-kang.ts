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
 * https://leetcode.com/problems/serialize-and-deserialize-binary-tree
 * T.C. O(n)
 * S.C. O(n)
 */
function serialize(root: TreeNode | null): string {
  return JSON.stringify(root);
}

function deserialize(data: string): TreeNode | null {
  return JSON.parse(data);
}

/**
 * Recursive
 * T.C. O(n)
 * S.C. O(n)
 */
function serialize(root: TreeNode | null): string {
  return root
    ? `${root.val},${serialize(root.left)},${serialize(root.right)}`
    : 'null';
}

function deserialize(data: string): TreeNode | null {
  const values = data.split(',');
  let index = 0;

  function dfs(): TreeNode | null {
    const val = values[index++];
    if (val === 'null') return null;

    const node = new TreeNode(parseInt(val));
    node.left = dfs();
    node.right = dfs();
    return node;
  }

  return dfs();
}
