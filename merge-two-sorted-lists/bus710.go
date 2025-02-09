package hello

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil && list2 == nil {
		return nil
	} else if list1 == nil {
		return list2
	} else if list2 == nil {
		return list1
	}

	newList := &ListNode{}
	cur := newList

	for {
		switch {
		case list1.Val < list2.Val:
			cur.Next = &ListNode{Val: list1.Val}
			list1 = list1.Next
		case list1.Val > list2.Val:
			cur.Next = &ListNode{Val: list2.Val}
			list2 = list2.Next
		default:
			cur.Next = &ListNode{Val: list1.Val}
			list1 = list1.Next
			cur = cur.Next
			cur.Next = &ListNode{Val: list2.Val}
			list2 = list2.Next
		}
		cur = cur.Next
		if list1 == nil && list2 == nil && cur.Next == nil {
			break
		}

		if list1 == nil {
			cur.Next = list2
			break
		}
		if list2 == nil {
			cur.Next = list1
			break
		}

	}

	return newList.Next
}
