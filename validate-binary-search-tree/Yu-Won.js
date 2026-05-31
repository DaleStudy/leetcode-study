/**
 * 문제: https://leetcode.com/problems/validate-binary-search-tree/description/
 *
 * 요구사항:
 * root 이진 트리 구조가 주어졌을 때, 해당 트리가 유효한 BST인지 판별하라.
 *
 * * */

const isValidBST = (nums) => {
    const validate = (node, min, max) => {
        if (!node) return true;

        if (node.val <= min || node.val >= max) return false;

        return validate(node.left, min, node.val) &&
            validate(node.right, node.val, max);
    }

    return validate(root, -Infinity, Infinity);
}
