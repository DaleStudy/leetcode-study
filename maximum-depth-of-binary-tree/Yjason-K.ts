/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/**
 * 이진 트리의 최대 깊이를 계산하는 함수
 * @param {TreeNode | null} root - 트리의 루트 노드
 * @returns {number} - 트리의 최대 깊이 (최상위 루트에서 가장 깊은 리프까지 깊이)
 *
 * 시간 복잡도: O(n)
 *  - 모든 노드를 한 번씩 방문하여 깊이를 계산
 *
 * 공간 복잡도: O(h) (h - 트리의 높이)
 */
function maxDepth(root: TreeNode | null): number {
    if (!root) return 0; // 노드가 없으면 깊이는 0

    return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1; // 왼쪽, 오른쪽 서브트리 중 더 깊은 값에 +1
};

