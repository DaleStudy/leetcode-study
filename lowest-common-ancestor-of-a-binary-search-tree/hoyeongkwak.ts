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
Time Complexity: O(logn)
Space Complexity: O(1)
*/
function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    if (!root || !p || !q) return null;
	let node = root
    while (node) {
        if (p.val < node.val && q.val < node.val) {
            node = node.left
        } else if (p.val > node.val && q.val > node.val) {
            node = node.right
        } else {
            return node
        }
    }
    return null
};
