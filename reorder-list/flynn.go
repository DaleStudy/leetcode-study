/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reorderList(head *ListNode) {
	// find a middle node
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	// reverse the second part of the list
	var prev, curr *ListNode = nil, slow
	for curr != nil {
		tmp := curr.Next
		curr.Next = prev
		prev = curr
		curr = tmp
	}
	// merge two parts of the list
	for curr1, curr2 := head, prev; curr2.Next != nil; {
		tmp1, tmp2 := curr1.Next, curr2.Next
		curr1.Next, curr2.Next = curr2, curr1.Next
		curr1, curr2 = tmp1, tmp2
	}
}
