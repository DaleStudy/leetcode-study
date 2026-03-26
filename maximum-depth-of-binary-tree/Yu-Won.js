/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 *
 * 문제: https://leetcode.com/problems/maximum-depth-of-binary-tree/
 * 요구사항: 이진 트리의 최대 깊이를 반환하라.
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
const maxDepth = (root) => {
    if(!root) return 0;

    let queue = [root];
    let depth = 0;

    while(queue.length) {
        let size = queue.length;

        for(let i = 0; i < size; i++) {
            let node = queue.shift();

            if(node.left) queue.push(node.left);
            if(node.right) queue.push(node.right);
        }
        depth++;
    }
    return depth;
};
