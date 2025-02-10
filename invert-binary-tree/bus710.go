package hello

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}

	visit(root)

	return root
}

func visit(node *TreeNode) {
	if node.Left != nil {
		visit(node.Left)
	}
	if node.Right != nil {
		visit(node.Right)
	}

	// Swap
	tmp := node.Left
	node.Left = node.Right
	node.Right = tmp
}
