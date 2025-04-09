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
 *
 * 문제가 너무 이해가 안감.. 처음보는 개념 너무 어려움
 *
 * 우선 이진트리에 대해서 공부해보기 위해서 https://www.youtube.com/watch?v=i57ZGhOVPcI 을 살펴보았음
 *
 * 풀이 1
 *
 * 재귀적 깊이 우선 탐색(DFS) 방식으로 해결 (메모리 효율성 미세하게 좋음) => 이 방법이 이진트리 개념에 조금 더 직관적임
 *
 * function isValidBST(root: TreeNode | null): boolean {
 *     function validate(node: TreeNode | null, min: number | null, max: number | null): boolean {
 *         if (node === null) return true;
 *
 *         if ((min !== null && node.val <= min) || (max !== null && node.val >= max)) {
 *             return false;
 *         }
 *
 *         return validate(node.left, min, node.val) && validate(node.right, node.val, max);
 *     }
 *
 *     return validate(root, null, null);
 * }
 *
 * 풀이 2
 *
 * 중위 순회 방법을 활용해보기 => 코드는 이 방법이 더 쉽고 이해하기 좋음
 */

function isValidBST(root: TreeNode | null): boolean {
    let prev: number | null = null;

    // 중위 순회를 수행합니다
    function inorder(node: TreeNode | null): boolean {
        if (node === null) return true;

        // 왼쪽 서브트리 검사
        if (!inorder(node.left)) return false;

        // 현재 노드 검사 (중위 순회에서 현재 값은 이전 값보다 커야 함)
        if (prev !== null && node.val <= prev) {
            return false;
        }
        prev = node.val;

        // 오른쪽 서브트리 검사
        return inorder(node.right);
    }

    return inorder(root);
}
