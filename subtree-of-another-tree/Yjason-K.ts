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
 * subTree가 root의 포함되는지 확인하는 함수
 * 
 * @param {TreeNode | null} root - 주어진 트리
 * @param {TreeNode | null} subRoot - 포함되는지 확인할 트리
 * @returns {boolean} - subRoot가 root에 포함되는지 여부
 * 
 * 시간 복잡도: O(n * m)
 * - `isSameTree`는 두 트리가 동일한지 확인하는데 O(m) 시간이 걸림 (`m`: subRoot의 노드 수).
 * - `isSubtree`는 `root`의 각 노드에서 `isSameTree`를 호출할 수 있음 (`n`: root의 노드 수).
 * - 따라서 최악의 경우 O(n * m).
 * 
 * 공간 복잡도: O(n)
 * - 재귀 호출에 따른 call stack 사용
 */
function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    if (!subRoot) return true;
    if (!root) return false;

    const isSameTree = (treeA: TreeNode | null, treeB: TreeNode | null ): boolean => {
        // 두 트리 모두 null 인 경우 true
        if (!treeA && !treeB) return true;
        // 하나만 null 인 경우 false
        if (!treeA || !treeB) return false;
        // val이 다른 경우 false
        if (treeA.val !== treeB.val) return false;
        return isSameTree(treeA.left, treeB.left) && isSameTree(treeA.right, treeB.right)
    } 

    // 현재 노드에서 subRoot가 시작되는 트리인지 확인
    if (isSameTree(root, subRoot)) return true;

    // 왼쪽, 오른쪽 하위 트에 subRoot가 포함되는지 확인
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
};

