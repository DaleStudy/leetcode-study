package hello

import (
	"errors"
	"log"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 1 {
		return &TreeNode{
			Val: preorder[0],
		}
	}

	center, _ := findCenterWithValue(preorder[0], inorder)

	head := TreeNode{
		Val: inorder[center],
	}

	execute(&head, center, inorder)

	return &head
}

func findCenterWithValue(key int, inorder []int) (int, error) {
	for i, n := range inorder {
		if n == key {
			return i, nil
		}
	}
	return 0, errors.New("not found")
}

func findCenter(slice []int) int {
	c := len(slice) / 2
	return c
}

func getSplit(center int, inorder []int, currentVal int) ([]int, []int) {
	if len(inorder) == 1 {
		if inorder[0] == currentVal {
			return nil, nil
		}
		return []int{inorder[0]}, nil
	}
	if len(inorder) == 2 {
		if inorder[0] == currentVal {
			return nil, []int{inorder[1]}
		}
		if inorder[1] == currentVal {
			return []int{inorder[0]}, nil
		}
		return []int{inorder[0]}, []int{inorder[1]}
	}
	return inorder[:center], inorder[center+1:]
}

func execute(currentNode *TreeNode, center int, slice []int) {
	left, right := getSplit(center, slice, currentNode.Val)

	if len(left) == 1 {
		currentNode.Left = &TreeNode{Val: left[0]}
	} else if len(left) == 2 {
		currentNode.Left = &TreeNode{Val: left[0]}
		currentNode.Left.Right = &TreeNode{Val: left[1]}
	} else if len(left) > 2 {
		lc := findCenter(left)
		currentNode.Left = &TreeNode{Val: left[lc]}

		if len(left) > 2 {
			execute(currentNode.Left, lc, left)
		}
	}

	if len(right) == 1 {
		currentNode.Right = &TreeNode{Val: right[0]}
	} else if len(right) == 2 {
		currentNode.Right = &TreeNode{Val: right[0]}
		currentNode.Right.Left = &TreeNode{Val: right[1]}
	} else if len(right) > 2 {
		rc := findCenter(right)
		currentNode.Right = &TreeNode{Val: right[rc]}

		if len(right) > 2 {
			execute(currentNode.Right, rc, right)
		}
	}
}

func print(currentNode *TreeNode) {
	log.Println(currentNode.Val)
	if currentNode.Left != nil {
		print(currentNode.Left)
	}
	if currentNode.Right != nil {
		print(currentNode.Right)
	}
}
