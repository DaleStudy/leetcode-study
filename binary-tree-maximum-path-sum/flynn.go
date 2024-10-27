/*
풀이
- post order traversal dfs를 활용하여 풀이할 수 있습니다
Big O
- N: node의 개수
- H: Tree의 높이
- Time compleixty: O(N)
  - 모든 node를 최대 한 번 탐색합니다
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
 func maxPathSum(root *TreeNode) int {
	res := root.Val

	var maxSubtreeSum func(*TreeNode) int
	maxSubtreeSum = func(node *TreeNode) int {
		// base case
		if node == nil {
			return 0
		}
		// left subtree로 내려갔을 때 구할 수 있는 maximum path sum
		// left subtree로 path를 내려갔을 때, left subtree가 sum에 기여하는 값이 0보다 작을 경우
		// left subtree로는 path를 내려가지 않는 것이 좋음
		// 따라서 left < 0 인 경우엔 left = 0
		left := maxSubtreeSum(node.Left)
		if left < 0 {
			left = 0
		}
		// right subtree도 left subtree와 동일함
		right := maxSubtreeSum(node.Right)
		if right < 0 {
			right = 0
		}
		// 현재 탐색하고 있는 node의 조상 node를 path에 포함하지 않고도
		// maxPathSum이 구해지는 경우가 있음
		if res < left+right+node.Val {
			res = left + right + node.Val
		}
		// 현재까지 계산한 subtree path sum을 부모 node에게 전달해야 함
		// 현재 node의 부모와 이어지는 path여야 하므로, node.Val + max(left, right)를 반환하면 됨
		subTreeSum := node.Val
		if left > right {
			subTreeSum += left
		} else {
			subTreeSum += right
		}
		return subTreeSum
	}

	maxSubtreeSum(root)
	return res
}
