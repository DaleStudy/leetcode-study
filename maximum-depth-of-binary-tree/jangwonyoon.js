/**
 * 104. Maximum Depth of Binary Tree
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/
 *
 */

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
 * @return {number}
 */

/*
 * 시간 복잡도(TC): O(n)
 * 공간 복잡도(SC): O(n)
 *
 * 관련 알고리즘: 분할 정복 Divide and Conquer, 재귀 Recursion
 *
 * 문제 풀이 방법:
 * 1. 루트 노드가 없으면 0을 반환
 * 2. 루트 노드의 왼쪽 서브트리의 최대 깊이를 계산
 * 3. 루트 노드의 오른쪽 서브트리의 최대 깊이를 계산
 * 4. 루트 노드의 왼쪽 서브트리의 최대 깊이와 오른쪽 서브트리의 최대 깊이 중 더 큰 값을 반환
 * 5. 루트 노드의 왼쪽 서브트리의 최대 깊이와 오른쪽 서브트리의 최대 깊이 중 더 큰 값에 1을 더하여 반환
 */

var maxDepth = function(root) {
    // 루트 노드가 없으면 0을 반환
    if (!root) return 0;

    // 루트 노드의 왼쪽 서브트리의 최대 깊이를 계산
    let left = maxDepth(root.left);
    // 루트 노드의 오른쪽 서브트리의 최대 깊이를 계산
    let right = maxDepth(root.right);

    // 루트 노드의 왼쪽 서브트리의 최대 깊이와 오른쪽 서브트리의 최대 깊이 중 더 큰 값을 반환
    // 루트 노드의 왼쪽 서브트리의 최대 깊이와 오른쪽 서브트리의 최대 깊이 중 더 큰 값에 1을 더하여 반환
    return Math.max(left, right) + 1;
};
