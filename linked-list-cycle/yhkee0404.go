/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    u := head
    v := head
    for u != nil && v != nil { // T(n) = O(n), S(n) = O(1)
        u = u.Next
        if (u == nil) {
            break
        }
        u = u.Next // https://hyp.is/gLsBIOHBEe6E_9M9T5MJNw/yhkee0404.github.io/posts/algorithms/leetcode/linked-list-cycle/
        v = v.Next
        if u == v {
            return true
        }
    }
    return false
}
