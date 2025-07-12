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

function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    if (preorder == null || inorder == null || preorder.length === 0 || inorder.length === 0) {
        return null
    } 

    const inorderMap = new Map()
    for (let i = 0 ; i < inorder.length; i++) {
        inorderMap.set(inorder[i], i)
    }

    const build = (preStart, preEnd, inStart, inEnd): TreeNode => {
        if (preStart > preEnd || inStart > inEnd) {
            return null
        }

        const rootVal = preorder[preStart]
        const root = new TreeNode(rootVal)

        const rootIndex = inorderMap.get(rootVal)
        const leftSize = rootIndex - inStart

        root.left = build(
            preStart + 1,
            preStart + leftSize,
            inStart,
            rootIndex - 1
        )

        root.right = build(
            preStart + leftSize + 1,
            preEnd,
            rootIndex + 1,
            inEnd
        )
        return root
    }
    return build(0, preorder.length - 1, 0, inorder.length - 1)
};
