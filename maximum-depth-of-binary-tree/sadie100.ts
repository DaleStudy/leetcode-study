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
 DFS로 노드를 탐색해가며 최대깊이를 찾는다
 
 시간 복잡도 : O(N - binary tree의 깊이)

 */

function maxDepth(root: TreeNode | null): number {
  let result = 0
  const search = (node, floor) => {
    if (!node) return
    result = Math.max(floor, result)

    search(node.left, floor + 1)
    search(node.right, floor + 1)
  }

  search(root, 1)
  return result
}
