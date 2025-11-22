package youngDaLee

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	return dfs(root, math.MinInt, math.MaxInt)
}

func dfs(node *TreeNode, min, max int) bool {
	if node == nil {
		return true
	}
	if (min < node.Val && node.Val < max) == false {
		return false
	}

	return dfs(node.Left, min, node.Val) && dfs(node.Right, node.Val, max)
}
