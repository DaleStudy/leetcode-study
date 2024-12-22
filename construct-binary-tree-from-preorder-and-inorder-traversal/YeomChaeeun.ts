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
 * 이진트리 만들기
 * 알고리즘 복잡도:
 * - 시간복잡도: O(n^2)
 * - 공간복잡도: O(n^2)
 */
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    // 전위 순회(preorder): 최상위 노드 -> 좌측 서브트리 -> 우측 서브트리
    // 중위 순회(inorder): 좌측 서브트리 -> 최상위 노드 -> 우측 서브트리

    // 재귀적으로 호출하기 위해 배열이 비었을때 null을 반환하며 종료시킴
    if (preorder.length === 0 || inorder.length === 0) {
        return null
    }

    let root = preorder[0]
    let mid = inorder.findIndex((value) => value === root)

    let leftInorder = inorder.slice(0, mid)
    let rightInorder = inorder.slice(mid+1)

    let leftPreorder = preorder.slice(1, 1 + leftInorder.length)
    let rightPreorder = preorder.slice(1 + leftInorder.length)

    let left = buildTree(leftPreorder, leftInorder)
    let right = buildTree(rightPreorder, rightInorder)

    return new TreeNode(root, left, right)
}
