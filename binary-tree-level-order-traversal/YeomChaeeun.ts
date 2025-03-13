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
 * 이진트리 레벨 순회 하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param root
 */
function levelOrder(root: TreeNode | null): number[][] {
  if(!root) return []
  let result = []
  const queue: TreeNode[] = [root]

  while (queue.length > 0) {
    const levelValues: number[] = []

    // 현재 레벨의 크기 (현재 큐에 있는 현재 레벨에 속한 노드의 수) 만큼 순회
    for (let i = 0; i < queue.length; i++) {
      const node = queue.shift()!

      // 현재 노드의 값을 현재 레벨의 값 배열에 추가
      levelValues.push(node.val)

      if (node.left) {
        queue.push(node.left);
      }
      if (node.right) {
        queue.push(node.right);
      }
    }

    result.push(levelValues)
  }

  return result;
}
