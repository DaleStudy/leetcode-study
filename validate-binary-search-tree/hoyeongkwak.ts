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
space complexity : O(n)
*/
function isValidBST(root: TreeNode | null): boolean {
    let prev = -Infinity
    let isValid = true
    const inOrder = (node: TreeNode | null): void => {
        if (!isValid || !node) return
        inOrder(node.left)
        
        if (prev >= node.val) {
            isValid = false
            return
        }
        prev = node.val
        inOrder(node.right)
    }
    inOrder(root)
    return isValid
}
