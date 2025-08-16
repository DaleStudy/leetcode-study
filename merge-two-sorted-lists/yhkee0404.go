/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    ans := &ListNode{}
    l1 := list1
    l2 := list2
    l3 := ans
    for l1 != nil || l2 != nil {
        if l2 == nil || l1 != nil && l1.Val < l2.Val {
            l3.Next = l1
            l1 = l1.Next
        } else {
            l3.Next = l2
            l2 = l2.Next
        }
        l3 = l3.Next
    }
    return ans.Next
}
