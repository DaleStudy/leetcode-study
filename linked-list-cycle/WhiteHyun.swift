//
//  141. Linked List Cycle.swift
//  https://leetcode.com/problems/linked-list-cycle/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/05/04.
//

import Foundation

final class LeetCode141 {
  func hasCycle(_ head: ListNode?) -> Bool {
    guard head != nil, head?.next != nil
    else {
      return false
    }

    var tortoise = head
    var hare = head?.next

    while hare != nil, hare?.next != nil {
      if tortoise === hare { return true }
      tortoise = tortoise?.next
      hare = hare?.next?.next
    }

    return false
  }
}
