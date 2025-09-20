/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

extension ListNode: Equatable {
    public static func == (lhs: ListNode, rhs: ListNode) -> Bool {
        return lhs === rhs
    }
}

extension ListNode: Hashable {
    public func hash(into hasher: inout Hasher) {
        hasher.combine(ObjectIdentifier(self))
    }
}

class Solution {
    // O(n) time / O(n) space
    func hasCycle(_ head: ListNode?) -> Bool {
        var visitedNodes = Set<ListNode>()
        var node = head
        
        while node != nil {
            guard let currentNode = node else {
                return false
            }
            
            if visitedNodes.contains(currentNode) {
                return true
            }
            
            visitedNodes.insert(currentNode)
            node = currentNode.next
        }
        
        return false
    }
    
    // O(n) time / O(1) space
    func hasCycleFloyd(_ head: ListNode?) -> Bool {
        var slow = head
        var fast = head
        
        while fast != nil && fast?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
            
            if slow === fast {
                return true
            }
        }
        
        return false
    }
}
