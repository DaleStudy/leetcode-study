public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    // Time O(n)
    // Space O(1)
    func reorderList(_ head: ListNode?) {
        guard let head = head, head.next != nil, head.next?.next != nil else {
            return
        }
        
        var slow = head
        var fast = head
        
        while fast.next != nil && fast.next?.next != nil {
            slow = slow.next!
            fast = fast.next!.next!
        }
        
        let secondHalf = slow.next
        slow.next = nil
        
        let reversedSecondHalf = reverseList(secondHalf)
        
        mergeLists(head, reversedSecondHalf)
    }
    
    private func reverseList(_ head: ListNode?) -> ListNode? {
        var prev: ListNode? = nil
        var current = head
        
        while current != nil {
            let nextTemp = current?.next
            current?.next = prev
            prev = current
            current = nextTemp
        }
        
        return prev
    }
    
    private func mergeLists(_ list1: ListNode?, _ list2: ListNode?) {
        var first = list1
        var second = list2
        
        while first != nil && second != nil {
            let firstNext = first?.next
            let secondNext = second?.next
            
            first?.next = second
            second?.next = firstNext
            
            first = firstNext
            second = secondNext
        }
    }
}
 
