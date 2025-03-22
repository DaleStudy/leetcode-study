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

function isValidBST(root: TreeNode | null): boolean {
    if (!root) return true;
    
    function isValid(node: TreeNode | null, min: number, max: number): boolean {
        if (!node) return true;
        if (node.val <= min || node.val >= max) return false;
        
        return isValid(node.left, min, node.val) && 
               isValid(node.right, node.val, max)
    }

    // 초기 호출 (루트 노드의 범위는 무한대)
    return isValid(root, -Infinity, Infinity)
}