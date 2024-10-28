/*
풀이
- 재귀함수를 이용해서 풀이할 수 있습니다
Big O
- N: 트리 노드의 개수
- H: 트리의 높이 (logN <= H <= N)
- Time complexity: O(N)
  - 모든 노드를 최대 1번 탐색합니다
- Space complexity: O(H)
  - 재귀 호출 스택의 깊이는 H에 비례하여 증가합니다
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func isSameTree(p *TreeNode, q *TreeNode) bool {
	// base case
	if p == nil && q == nil {
		return true
	} else if p == nil || q == nil {
		return false
	}

	if p.Val != q.Val {
		return false
	}

	if !isSameTree(p.Left, q.Left) || !isSameTree(p.Right, q.Right) {
		return false
	}

	return true
}
