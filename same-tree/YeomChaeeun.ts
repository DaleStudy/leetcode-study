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
 * 같은 트리인지 확인하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param p
 * @param q
 */
function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
  if(!p || !q) {
    return p === q;
  }

  return p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)

}
