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
Time Complexity: O(n)
Space Complexity: O(n)
*/
function levelOrder(root: TreeNode | null): number[][] {
    if (root == null) return []
    const result: number[][] = []
    let queue: TreeNode[] = [root]
    while (queue.length > 0) {
        const levelSize = queue.length
        const currentLevel: number[] = []
        for(let i = 0; i< levelSize; i++) {
            const node = queue.shift()!
            currentLevel.push(node.val)

            if (node.left) queue.push(node.left)
            if (node.right) queue.push(node.right)
        }
        result.push(currentLevel)
    }
    return result
}
