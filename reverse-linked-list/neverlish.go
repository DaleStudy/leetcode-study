// 시간복잡도: O(n)
// 공간복잡도: O(1)

package main

import "testing"

func TestReverseList(t *testing.T) {
	result1 := reverseList(&ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 3,
				Next: &ListNode{
					Val: 4,
					Next: &ListNode{
						Val:  5,
						Next: nil,
					},
				},
			},
		},
	})

	if result1.Val != 5 {
		t.Errorf("Expected 5, but got %v", result1.Val)
	}

	if result1.Next.Val != 4 {
		t.Errorf("Expected 4, but got %v", result1.Next.Val)
	}

	if result1.Next.Next.Val != 3 {
		t.Errorf("Expected 3, but got %v", result1.Next.Next.Val)
	}

	if result1.Next.Next.Next.Val != 2 {
		t.Errorf("Expected 2, but got %v", result1.Next.Next.Next.Val)
	}

	if result1.Next.Next.Next.Next.Val != 1 {
		t.Errorf("Expected 1, but got %v", result1.Next.Next.Next.Next.Val)
	}
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode

	for head != nil {
		next := head.Next
		head.Next = prev
		prev = head
		head = next
	}

	return prev
}
