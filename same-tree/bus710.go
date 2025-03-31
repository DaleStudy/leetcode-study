package hello

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}

	return checker(p, q)
}

func checker(p, q *TreeNode) bool {
	if eitherNilChecker(p, q) {
		return false
	}

	if p.Val != q.Val {
		return false
	}

	if !bothNilChecker(p.Left, q.Left) {
		re := checker(p.Left, q.Left)
		if !re {
			return false
		}
	}
	if !bothNilChecker(p.Right, q.Right) {
		re := checker(p.Right, q.Right)
		if !re {
			return false
		}
	}

	return true
}

func eitherNilChecker(p, q *TreeNode) bool {
	if p == nil && q != nil {
		return true
	}
	if p != nil && q == nil {
		return true
	}
	if p.Left != nil && q.Left == nil {
		return true
	}
	if p.Left == nil && q.Left != nil {
		return true
	}
	if p.Right != nil && q.Right == nil {
		return true
	}
	if p.Right == nil && q.Right != nil {
		return true
	}
	return false
}

func bothNilChecker(p, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	return false
}
