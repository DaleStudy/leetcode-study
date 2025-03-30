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
 * 트리 내에 동일한 서브트리가 있는지 찾는 알고리즘
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n×m) - n(root 노드 수), m(subRoot 노드 수)
 * - 공간 복잡도: O(n+m) - 첫 번째 isSubtree()의 호출 스택의 깊이와 isSameTree()의 호출 스택의 깊이를 더한 것
 * @param root
 * @param subRoot
 */
function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    if(!subRoot) return true
    if(!root) return false

    // 이전에 풀이한 isSameTree를 추가
    function isSameTree(p: TreeNode | null, q: TreeNode | null) {
        if(!p || !q) {
            return p === q;
        }
        return p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    }

    if (isSameTree(root, subRoot)) return true
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
}

