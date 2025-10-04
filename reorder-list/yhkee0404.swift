/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func reorderList(_ head: ListNode?) {
        let temp = ListNode(0, head)
        solve(temp, temp, false)
    }
    func solve(_ tortoise: ListNode, _ hare: ListNode?, _ odd: Bool) -> ListNode? {
        guard let safeHare = hare else {
            let tail = ListNode(0, tortoise.next)
            tortoise.next = nil
            return tail
        }
        let tail = solve(odd ? tortoise : tortoise.next!, safeHare.next, !odd)
        if !odd {
            return tail
        }
        guard let safeTail = tail else {
            return nil
        }
        if safeTail.val == 0 {
            return safeTail.next
        }
        let next = safeTail.next
        safeTail.next = tortoise.next
        tortoise.next = safeTail
        return next
    }
}
