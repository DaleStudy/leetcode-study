//  
//  19. Remove Nth Node From End of List
//  https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/10.
//  

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
  func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
    let answerNode = ListNode(0, head)
    var footprintNode = head

    for _ in 0 ..< n {
      footprintNode = footprintNode?.next
    }

    var targetNode: ListNode? = answerNode
    while footprintNode != nil {
      targetNode = targetNode?.next
      footprintNode = footprintNode?.next
    }
    targetNode?.next = targetNode?.next?.next

    return answerNode.next
  }
}
