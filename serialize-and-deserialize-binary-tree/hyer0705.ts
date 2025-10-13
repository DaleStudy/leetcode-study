/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
  if (!root) return "null";

  let result = "" + root.val;

  result += "," + serialize(root.left);
  result += "," + serialize(root.right);

  return result;
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
  const values = data.split(",");
  let index = 0;

  const buildTree = () => {
    const val = values[index];
    index++;

    if (val === "null") return null;

    const node = new TreeNode(Number(val));
    node.left = buildTree();
    node.right = buildTree();
    return node;
  };

  return buildTree();
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
