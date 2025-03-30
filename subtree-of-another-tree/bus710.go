package hello

import "testing"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil || subRoot == nil {
		return false
	}

	return search(root, subRoot)
}

func search(r *TreeNode, sr *TreeNode) bool {
	if r.Val == sr.Val {
		if ret := compare(r, sr); ret {
			return ret
		}
	}

	if r.Left != nil {
		if ret := search(r.Left, sr); ret {
			return ret
		}
	}

	if r.Right != nil {
		if ret := search(r.Right, sr); ret {
			return ret
		}
	}

	return false
}

func compare(r *TreeNode, sr *TreeNode) bool {
	if r.Val == sr.Val {
		if r.Left != nil && sr.Left != nil {
			if ret := compare(r.Left, sr.Left); !ret {
				return false
			}
		} else if r.Left != nil && sr.Left == nil {
			return false
		} else if r.Left == nil && sr.Left != nil {
			return false
		}

		if r.Right != nil && sr.Right != nil {
			if ret := compare(r.Right, sr.Right); !ret {
				return false
			}
		} else if r.Right != nil && sr.Right == nil {
			return false
		} else if r.Right == nil && sr.Right != nil {
			return false
		}
	} else {
		return false
	}

	return true
}

func Test_isSubtree(t *testing.T) {
	t1a, t1b := test01()

	type args struct {
		root    *TreeNode
		subRoot *TreeNode
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "test 1",
			args: args{t1a, t1b},
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isSubtree(tt.args.root, tt.args.subRoot); got != tt.want {
				t.Errorf("isSubtree() = %v, want %v", got, tt.want)
			}
		})
	}
}

func test01() (*TreeNode, *TreeNode) {
	t3 := TreeNode{
		Val:   1,
		Left:  nil,
		Right: nil,
	}
	t4 := TreeNode{
		Val:   2,
		Left:  nil,
		Right: nil,
	}
	t1 := TreeNode{
		Val:   4,
		Left:  &t3,
		Right: &t4,
	}
	t2 := TreeNode{
		Val:   5,
		Left:  nil,
		Right: nil,
	}

	t0 := TreeNode{
		Val:   3,
		Left:  &t1,
		Right: &t2,
	}

	y1 := TreeNode{
		Val: 1,
	}
	y2 := TreeNode{
		Val: 2,
	}
	y0 := TreeNode{
		Val:   4,
		Left:  &y1,
		Right: &y2,
	}

	return &t0, &y0
}
