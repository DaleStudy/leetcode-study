// TC : O(n) n being the length of list
// SC : O(n) n being the size of the two list
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    // Create a dummy node to simplify edge cases
    dummy := &ListNode{}
    current := dummy

    // Merge lists
    for list1 != nil && list2 != nil {
        if list1.Val < list2.Val {
            current.Next = list1
            list1 = list1.Next
        } else {
            current.Next = list2
            list2 = list2.Next
        }
        current = current.Next
    }

    if list1 != nil {
        current.Next = list1
    } else {
        current.Next = list2
    }

    return dummy.Next
}
