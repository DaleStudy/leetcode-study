public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    // Time complexity O(n)
    // Space complexity O(1)
    func reverseList(_ head: ListNode?) -> ListNode? {
        var reverseList: ListNode? = nil
        var currentHead = head
        while let node = currentHead {
            currentHead = node.next
            node.next = reverseList
            reverseList = node
        }
        return reverseList
    }
}
 
