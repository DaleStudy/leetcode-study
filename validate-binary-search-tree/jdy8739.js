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
 */
var isValidBST = function (root) {
    const dfs = (node, min, max) => {
        if (!node) {
            return true;
        }
        
        if ((min !== undefined && node.val <= min) || (max !== undefined && node.val >= max)) {
            return false;
        }

        return dfs(node.left, min, node.val) && dfs(node.right, node.val, max);
    };

    return dfs(root, undefined, undefined);
};

// 시간복잡도 O(n) -> 최악의 경우인 완전한 이진 트리의 경우 모든 노드를 방문해서 확인해야 함
// 공간복잡도 o(h) -> 최대 트리의 높이만큼 함수호출 스택에 함수컨텍스트가 쌓임
