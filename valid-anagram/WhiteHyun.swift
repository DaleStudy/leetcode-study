//
//  242. Valid Anagram.swift
//  https://leetcode.com/problems/valid-anagram/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/04/26.
//

import Foundation

final class LeetCode242 {
  func isAnagram(_ s: String, _ t: String) -> Bool {
    Dictionary(s.map { ($0, 1) }, uniquingKeysWith: +) == Dictionary(t.map { ($0, 1) }, uniquingKeysWith: +)
  }
}
