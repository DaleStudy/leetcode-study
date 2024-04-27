//
//  217. Contains Duplicate.swift
//  https://leetcode.com/problems/contains-duplicate/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/04/26.
//

import Foundation

final class LeetCode217 {
  func containsDuplicate(_ nums: [Int]) -> Bool {
    Set(nums).count != nums.count
  }
}
