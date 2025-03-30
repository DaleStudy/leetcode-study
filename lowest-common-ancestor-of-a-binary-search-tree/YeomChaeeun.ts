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
 * BST 이진트리에 두 노드가 주어졌을 때, 근접한 부모 찾기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param root
 * @param p
 * @param q
 */
function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    if(root === null || p === null || q === null) return null;

    if(p.val < root.val && q.val < root.val) {
        return lowestCommonAncestor(root.left, p, q)
    } else if(p.val > root.val && q.val > root.val) {
        return lowestCommonAncestor(root.right, p, q)
    } else {
        // 현재 노드가 양쪽 방향으로 있거나 현재 노드가 p, q인 경우
        return root
    }
}
