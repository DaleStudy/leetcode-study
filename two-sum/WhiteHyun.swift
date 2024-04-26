//
//  1. Two Sum.swift
//  https://leetcode.com/problems/two-sum/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/04/26.
//

import Foundation

final class LeetCode1 {
  func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
    let sortedNumbersWithIndex = numbers.enumerated().sorted { lhs, rhs in
      lhs.element < rhs.element
    }
    var left = 0
    var right = sortedNumbersWithIndex.endIndex - 1

    while left < right {
      let sum = sortedNumbersWithIndex[left].element + sortedNumbersWithIndex[right].element
      if sum == target { break }
      if sum < target {
        left += 1
      } else {
        right -= 1
      }
    }

    return [sortedNumbersWithIndex[left].offset, sortedNumbersWithIndex[right].offset]
  }
}
