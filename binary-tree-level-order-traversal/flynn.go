/*
풀이
- queue 자료구조를 사용하여 풀이합니다
Big O
- N: 노드의 개수
- Time complexity: O(N)
  - 모든 노드를 조회합니다
- Space complexity: O(N)
  - 반환 결과값인 2차원 배열 levels -> O(N)
  - queue -> O(3/4 * N) = O(N)
    - 한 층이 가질 수 있는 최대 노드 개수는 약 N / 2
	- queue의 크기가 가장 클 때는 두 층의 노드를 가지고 있으므로 N / 2 + (N / 2) / 2 개의 노드를 갖게 됨
  - level -> O(N/2) = O(N)
    - - 한 층이 가질 수 있는 최대 노드 개수는 약 N / 2
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func levelOrder(root *TreeNode) [][]int {
	levels := make([][]int, 0)

	if root == nil {
		return levels
	}

	queue := make([]*TreeNode, 0)
	queue = append(queue, root)
	for len(queue) > 0 {
		k := len(queue)
		level := make([]int, k)
		for i := 0; i < k; i++ {
			node := queue[i]
			level[i] = node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		queue = queue[k:]
		levels = append(levels, level)
	}

	return levels
}
