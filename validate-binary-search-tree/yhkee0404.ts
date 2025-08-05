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

function isValidBST(root: TreeNode | null, left = - (1 << 30) * 2, right = - (left + 1)): boolean {
    return root === null || root.val >= left && root.val <= right
            && (root.left === null || root.val != (- (1 << 30) * 2) && isValidBST(root.left, left, root.val - 1))
            && (root.right === null || root.val != - (- (1 << 30) * 2 + 1) && isValidBST(root.right, root.val + 1, right))
};
