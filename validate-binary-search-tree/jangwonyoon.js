/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 *
 * DFS를 사용하여 왼쪽 노드와 오른쪽 노드를 검증한다.
 *
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
var isValidBST = function(root) {
    const MAX_VALUE = Infinity;
    const MIN_VALUE = -Infinity;

    const validate = (node, min, max) => {
        // 재귀 탈출 조건
        if (!node) return true;

        // 예외 처리 - 현재 노드의 값이 최소값보다 작거나 최대값보다 크면 예외 처리
        if (node.val <= min || node.val >= max) return false;

        const leftNode = node.left;
        const rightNode = node.right;

        // 왼쪽 노드 검증 - 현재 값이 제일 크고, 왼쪽은 본인보다 작아야한다.
        const validateLeftNode = validate(leftNode, min , node.val);

        // 오른쪽 노드 검증 - 현재 값이 제일 작으며, 우측 노드 값이 본인 보다 커야한다.
        const validateRightNode = validate(rightNode, node.val, max)

        return validateLeftNode && validateRightNode;
    }

    return validate(root, MIN_VALUE, MAX_VALUE);
};
