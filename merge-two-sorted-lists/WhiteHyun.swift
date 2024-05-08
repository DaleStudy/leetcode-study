//
//  21. Merge Two Sorted Lists.swift
//  https://leetcode.com/problems/merge-two-sorted-lists/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/05/04.
//

import Foundation

final class LeetCode21 {
  func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
    let dummy: ListNode? = .init(0)
    var currentNode: ListNode? = dummy
    var l1 = list1
    var l2 = list2

    while l1 != nil, l2 != nil {
      if l1!.val < l2!.val {
        currentNode?.next = l1
        l1 = l1?.next
      } else {
        currentNode?.next = l2
        l2 = l2?.next
      }

      currentNode = currentNode?.next
    }

    currentNode?.next = l1 ?? l2

    return dummy?.next
  }
}
