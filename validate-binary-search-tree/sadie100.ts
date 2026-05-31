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

/*
큐를 만들고 루트에서 아래로 내려가면서 노드, max값(left로 빠질 때 현재 노드값으로 갱신), min값(right로 빠질 때 현재 노드값으로 갱신)을 전달하고,
하나씩 꺼내면서 min max 한도를 검사, 조건에 맞지 않는 노드가 있으면 false를 반환한다

시간복잡도 : O(N) (N은 트리의 노드 개수)
공간복잡도 : O(N) (queue 사용)
*/

function isValidBST(root: TreeNode | null): boolean {
  if (root === null) return true
  const queue: [TreeNode, number | null, number | null][] = [[root, null, null]]
  let idx = 0

  while (idx < queue.length) {
    const [node, min, max] = queue[idx]

    if (min !== null && node.val <= min) return false
    if (max !== null && node.val >= max) return false

    if (node.left) {
      queue.push([node.left, min, node.val])
    }
    if (node.right) {
      queue.push([node.right, node.val, max])
    }
    idx += 1
  }

  return true
}
