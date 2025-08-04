class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        var current = head, previous: ListNode? = nil

        while current != nil {
            let next = current?.next
            current?.next = previous
            previous = current
            current = next
        }

        return previous
    }
}
