//
//  206. Reverse Linked List.swift
//  https://leetcode.com/problems/reverse-linked-list/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/05/04.
//

import Foundation

final class LeetCode206 {
  func reverseList(_ node: ListNode?, _ prev: ListNode? = nil) -> ListNode? {
    guard let node else { return prev }

    let next = node.next
    node.next = prev

    return reverseList(next, node)
  }
}
