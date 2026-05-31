/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// TC: O(n)
// SC: O(1)
func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	cur := head

	for cur != nil {
		temp := cur.Next
		cur.Next = prev
		prev = cur
		cur = temp
	}
	return prev
}
