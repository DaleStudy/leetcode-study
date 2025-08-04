/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * 이진 탐색 트리(BST)인지 확인하는 함수
 * @param {TreeNode} root
 * @return {boolean}
 */

///////////////////////// 1 ///////////////////////////
// inorder traversal한 결과를 배열에 담아 오름차순 정렬인지 확인
const isValidBST = function(root) {
    const inorder = [];
    inorderTraversal(root, inorder);

    return inorder.every((val, i, arr) => i === 0 || arr[i-1] < val);
};

function inorderTraversal(current, result) {
    if (current.left) {
        inorderTraversal(current.left, result);
    }

    result.push(current.val);

    if (current.right) {
        inorderTraversal(current.right, result);
    }
}

///////////////////////// 2 ///////////////////////////
// inorder traversal하면서 바로 직전에 순회한 값이 현재 값보다 작은지 확인 (=오름차순인지 바로바로 확인)
const isValidBST = function(root) {
    let prev = -Infinity;

    function inorder(node) {
        if (!node) return true;

        if (!inorder(node.left)) return false;

        if (node.val <= prev) return false;
        prev = node.val;

        return inorder(node.right);
    }

    return inorder(root);
};

// 시간복잡도: O(n)
// 공간복잡도: O(n) (재귀 스택 == 트리 높이. 최악의 경우 편향 트리일 때 높이는 n)
