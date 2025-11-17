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
    func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
        var slow: ListNode? = head
        var fast: ListNode? = head
        var prev: ListNode?
        
        for _ in 1...n {
            fast = fast?.next
        }
        
        while fast != nil {
            prev = slow
            slow = slow?.next
            fast = fast?.next
        }
        
        if prev != nil {
            prev?.next = slow?.next
        } else {
            return head?.next
        }
        
        return head
    }
}
 
