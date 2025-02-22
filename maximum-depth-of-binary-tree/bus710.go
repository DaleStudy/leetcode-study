package hello

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return count(root)
}

func count(node *TreeNode) int {
	if node == nil {
		return 0
	}

	lc := count(node.Left) + 1
	rc := count(node.Right) + 1

	if lc > rc {
		return lc
	}
	return rc
}
