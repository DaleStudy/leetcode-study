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
    // O(n) time / O(1) space
    func reverseList(_ head: ListNode?) -> ListNode? {
        var node = head
        var lastNode: ListNode? = nil
        
        while node != nil {
            let next = node?.next
            node?.next = lastNode
            lastNode = node
            node = next
        }
        
        return lastNode
    }
}
