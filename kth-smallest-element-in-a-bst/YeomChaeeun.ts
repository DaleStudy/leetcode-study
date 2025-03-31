/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left  = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
/**
 * Binary Search Tree 특성을 고려하여 k번째 작은 숫자를 찾기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 */
function kthSmallest(root: TreeNode | null, k: number): number {
    let count = 0;
    let result = 0;

    /*
    BST의 특성
    - 왼쪽 서브트리의 노드 값 < 현재 노드 값
    - 현재 노드값 < 왼쪽 서브트리의 노드 값
    => 중위 순회시 오름차 순 방문
    */

    // 중위 순회 함수
    function inorder(node: TreeNode | null): void {
        if (node === null) return;
        inorder(node.left);

        count++;
        if (count === k) {
            result = node.val;
            return;
        }

        inorder(node.right);
    }

    inorder(root);
    return result;
}
