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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
const isSubtree = function(root, subRoot) {
    const isSame = function(node1, node2) {
        if (!node1 && !node2) return true;
        if (node1?.val !== node2?.val) return false;

        return isSame(node1.left, node2.left) && isSame(node1.right, node2.right);
    }

    const queue = [root];

    while (queue.length) {
        const node = queue.shift();

        if (node.left) {
            queue.push(node.left);
        }

        if (node.right) {
            queue.push(node.right);
        }

        if (isSame(node, subRoot)) {
            return true;
        }
    }

    return false;
};

// 다른 접근법:
// 정렬해서 비교하는 방식 => left, right 구분이 안가는 문제
// 정렬할 때 left, right 정보를 포함해서 직렬화하면 됨
// 이렇게 하면 복잡도 면에서 성능이 더 좋음

// 시간복잡도: O(n * m) (n: root size, m: subroot size)
// 공간복잡도: O(n + m)
