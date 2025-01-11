// 시간복잡도: O(n)
// 공간복잡도: O(1)

package main

import "testing"

type ListNode struct {
	Val  int
	Next *ListNode
}

func TestMergeTwoLists(t *testing.T) {
	result1 := mergeTwoLists(&ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 4}}}, &ListNode{Val: 1, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4}}})
	if result1.Val != 1 || result1.Next.Val != 1 || result1.Next.Next.Val != 2 || result1.Next.Next.Next.Val != 3 || result1.Next.Next.Next.Next.Val != 4 || result1.Next.Next.Next.Next.Next.Val != 4 {
		t.Error("Test case 1 failed")
	}
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}

	if list2 == nil {
		return list1
	}

	if list1.Val < list2.Val {
		list1.Next = mergeTwoLists(list1.Next, list2)
		return list1
	} else {
		list2.Next = mergeTwoLists(list1, list2.Next)
		return list2
	}
}
