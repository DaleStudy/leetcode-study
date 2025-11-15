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

// 37ms
// Time Complexity: O(n^2), n: 노드의 수
// Space Complexity: O(h), h: 트리의 높이
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  if (preorder.length === 0 || inorder.length === 0) return null;

  const root = preorder[0];

  const rootIdx = inorder.findIndex((el) => el === root);

  const leftInorder = inorder.slice(0, rootIdx);
  const leftPreorder = preorder.slice(1, leftInorder.length + 1);

  const rightInorder = inorder.slice(rootIdx + 1);
  const rightPreorder = preorder.slice(leftInorder.length + 1);

  const rootNode = new TreeNode(root);

  rootNode.left = buildTree(leftPreorder, leftInorder);
  rootNode.right = buildTree(rightPreorder, rightInorder);

  return rootNode;
}

// 3ms
// Time Complexity: O(n), n: 노드의 수
// Space Complexity: O(n), n: 노드의 수
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  if (preorder.length === 0 || inorder.length === 0) return null;

  const indexMap = new Map<number, number>();
  inorder.forEach((node, idx) => indexMap.set(node, idx));

  const build = (preStart: number, preEnd: number, inStart: number, inEnd: number): TreeNode | null => {
    if (preStart > preEnd || inStart > inEnd) return null;

    const rootVal = preorder[preStart];
    const rootIdx = indexMap.get(rootVal);

    const leftSize = rootIdx - inStart;

    const root = new TreeNode(rootVal);
    root.left = build(preStart + 1, preStart + leftSize, inStart, rootIdx - 1);
    root.right = build(preStart + leftSize + 1, preEnd, rootIdx + 1, inEnd);

    return root;
  };

  return build(0, preorder.length - 1, 0, inorder.length - 1);
}
