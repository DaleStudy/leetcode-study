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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    const arr = [];

    const dfs = (node) => {
        arr.push(node.val);

        if (node?.left) {
            dfs(node.left);
        }

        if (node?.right) {
            dfs(node.right);
        }
    }

    dfs(root);

    const sort = arr.sort((a, b) => a - b);

    return sort[k - 1];
};

// 시간복잡도 -> O(nlogn) dfs로 노드의 val을 배열에 넣고 정렬하는 시간이 소요됨
// 공간복잡도 -> O(n) 리스트의 길이만큼 arr의 공간이 필요함
