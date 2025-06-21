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
 * Encodes a tree to a single string.
 */

// TC: O(n)
// SC: O(n)
function serialize(root: TreeNode | null): string {
  if (!root) return "null";
  return `${root.val},${serialize(root.left)},${serialize(root.right)}`;
}

/*
 * Decodes your encoded data to tree.
 */

// TC: O(n)
// SC: O(n)
function deserialize(data: string): TreeNode | null {
  const values = data.split(",");
  let idx = 0;

  const dfs = () => {
    if (values[idx] === "null") {
      idx++;
      return null;
    }

    const node = new TreeNode(parseInt(values[idx]));
    idx++;
    node.left = dfs();
    node.right = dfs();
    return node;
  };

  return dfs();
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
