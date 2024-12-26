package main

import "testing"

func TestBuildTree(t *testing.T) {
	preorder := []int{3,9,20,15,7}
	inorder := []int{9,3,15,20,7}

	result := buildTree(preorder, inorder)
	println(result.Val)
	println(result.Left.Val)
	println(result.Right.Val)
	println(result.Right.Left.Val)
	println(result.Right.Right.Val)
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findIndex(target int, values []int) int {
	for i, v := range values {
		if v == target {
			return i
		}
	}
	return -1
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(inorder) == 0 {
		return nil
	}
	Val := preorder[0]

	midIndex := findIndex(Val, inorder)

	Left := buildTree(preorder[1:midIndex+1], inorder[:midIndex])
	Right := buildTree(preorder[midIndex+1:], inorder[midIndex+1:])

	return &TreeNode{
		Val,
		Left,
		Right,
	}
}
