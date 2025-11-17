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
    func reorderListUsingArray(_ head: ListNode?) {
        var nodes = [ListNode]()
        var node = head
        while node != nil {
            nodes.append(node!)
            node = node!.next
        }
        
        node = head
        var fromFirstIndex = 1
        var fromLastIndex = nodes.count - 1
        
        while fromFirstIndex <= fromLastIndex {
            guard node != nil, nodes.last != nil else {
                break
            }
            node!.next = nodes.removeLast()
            node = node!.next
            
            guard fromFirstIndex < fromLastIndex else {
                break
            }
            
            fromLastIndex -= 1
            node!.next = nodes[fromFirstIndex]
            fromFirstIndex += 1
            node = node!.next
        }
        
        node?.next = nil
    }
    
    // O(n) time / O(1) space
    func reorderList(_ head: ListNode?) {
        func findMiddle(_ head: ListNode?) -> ListNode? {
            var slow = head
            var fast = head
            
            while fast?.next?.next != nil {
                slow = slow?.next
                fast = fast?.next?.next
            }
            
            return slow
        }
        
        var mid = findMiddle(head)
        
        func reverseList(_ head: ListNode?) -> ListNode? {
            var prev: ListNode? = nil
            var curr: ListNode? = head
            var next: ListNode? = curr?.next
            
            while curr != nil {
                curr?.next = prev

                prev = curr
                curr = next
                next = next?.next
            }
            
            return prev
        }
        
        let reversedToMid = reverseList(mid?.next)
        mid?.next = nil
        
        func mergeList(first: ListNode?, second: ListNode?) {
            var first = first
            var second = second
            
            while first != nil {
                let firstTmp = first?.next
                first?.next = second
                let secondTmp = second?.next
                second?.next = firstTmp
                
                first = firstTmp
                second = secondTmp
            }
        }
        
        mergeList(first: head, second: reversedToMid)
    }
}
