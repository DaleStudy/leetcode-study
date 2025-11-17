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
    // O(n) time / O(n) space
    func removeNthFromEndList(_ head: ListNode?, _ n: Int) -> ListNode? {
        var nodes = [ListNode]()
        var node = head
        while let current = node {
            nodes.append(current)
            node = current.next
        }
        
        let indexToRemove = nodes.count - n
        
        if indexToRemove == 0 {
            return head?.next
        }
        
        nodes[indexToRemove - 1].next = indexToRemove + 1 < nodes.count ? nodes[indexToRemove + 1] : nil
        return head
    }
    
    // O(n) time / O(1) space
    func removeNthFromEndPointer(_ head: ListNode?, _ n: Int) -> ListNode? {
        let dummy = ListNode(0)
        dummy.next = head
        var post: ListNode? = dummy
        var prev: ListNode? = dummy

        for _ in 0...n {
            post = post?.next
        }

        while post != nil {
            prev = prev?.next
            post = post?.next
        }

        prev?.next = prev?.next?.next
        return dummy.next
    }
}
