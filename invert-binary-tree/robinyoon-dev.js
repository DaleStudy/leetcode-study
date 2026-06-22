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
 * @return {TreeNode}
 */
var invertTree = function (root) {

    let node = root;

    let result = changeLeftAndRight(node);

    return result;

    function changeLeftAndRight(root) {
        // 종료 조건
        if (root === null) return root;

        tempLeft = root.left;
        tempRight = root.right;

        root.left = tempRight;
        root.right = tempLeft;

        changeLeftAndRight(root.left);
        changeLeftAndRight(root.right);

        return root;
    }
};
