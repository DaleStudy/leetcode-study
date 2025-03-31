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
 * 두 트리가 같은 객체 트리인지 확인하는 함수
 * @param {Treenode | null} p - 트리 노드 p 
 * @param {Treenode | null} q - 트리 노드 q
 * @returns {boolean} - 두 트리가 동일한 구조인지 여부
 * 
 * 시간 복잡도: O(n)
 * - 최대  두 트리의 모든 노드를 한 번씩만 방문
 * 공간 복잡도: O(n)
 * - 재귀 호출로 트리 깊이 만큼의 공간이 필요
 */
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    // 같은 객체를 가리키고 있는 경우 true
    if (p === q) return true;

    // 한쪽이 null 인 경우 false
    if (!p || !q) return false;

    // 두 노드가 다른 경우 false
    if(p.val !== q.val) return false;

    // 제귀를 통한 하위 트리 비교
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

