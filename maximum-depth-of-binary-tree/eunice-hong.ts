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

/**
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
function maxDepth(root: TreeNode | null): number {
    if (!root) {
        // tree is empty
        return 0
    } else if (!root.left && !root.right) {
        // tree has no children
        return 1
    } else {
        // tree has at least one child
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right))
    }
};