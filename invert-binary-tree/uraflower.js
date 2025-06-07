/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * 이진 트리를 좌우 반전하여 반환하는 함수
 * @param {TreeNode} root
 * @return {TreeNode}
 */
const invertTree = function (root) {
    if (root !== null) {
        invertTree(root.right);
        invertTree(root.left);
        [root.right, root.left] = [root.left, root.right];
    }

    return root;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
