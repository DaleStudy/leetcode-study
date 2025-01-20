package hello

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	head2 := &ListNode{}

	if head == nil {
		return nil
	}

	for {
		head2.Val = head.Val
		if head.Next == nil {
			break
		}
		head = head.Next
		temp := &ListNode{Next: head2}
		head2 = temp
	}

	return head2
}
