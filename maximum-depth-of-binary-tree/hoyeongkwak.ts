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
    time complexity : O(n)
    space complexity : O(logn)
*/

function maxDepth(root: TreeNode | null): number {
    if (root == null) return 0
    let maxLeft = maxDepth(root.left)
    let maxRight = maxDepth(root.right)
    return Math.max(maxLeft, maxRight) + 1
};
