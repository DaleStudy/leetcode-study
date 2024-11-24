/*
풀이
- n+1 간격을 유지하며 이동하는 두 개의 포인터를 이용하면 one-pass로 해결할 수 있습니다
Big O
- M: 링크드리스트의 길이
- Time complexity: O(M)
- Space complexity: O(1)
*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 func removeNthFromEnd(head *ListNode, n int) *ListNode {
	dummy := &ListNode{Next: head}

	slow := dummy
	fast := dummy
	for i := 0; i < n+1; i++ {
		fast = fast.Next
	}

	for fast != nil {
		slow = slow.Next
		fast = fast.Next
	}
	slow.Next = slow.Next.Next

	return dummy.Next
}
