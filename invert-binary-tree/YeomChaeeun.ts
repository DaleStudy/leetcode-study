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
 * 이진트리 좌우 반전하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param root
 */
function invertTree(root: TreeNode | null): TreeNode | null {

    // 1. 재귀 알고리즘
    // if(root === null) return null
    //
    // const right = root.right;
    // root.right = invertTree(root.left)
    // root.left = invertTree(right)
    //
    // return root

    // 2. 스택을 사용하여 트리를 순회 - 반복 알고리즘
    let stack : (TreeNode | null)[] = [root]
    while(stack.length > 0) {
        const node = stack.pop();
        if(!node) continue

        [node.left, node.right] = [node.right, node.left];

        stack.push(node.left)
        stack.push(node.right)
    }
    return root
}
