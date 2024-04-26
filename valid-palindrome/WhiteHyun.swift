//
//  125. Valid Palindrome.swift
//  https://leetcode.com/problems/valid-palindrome/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/04/26.
//

import Foundation

final class LeetCode125 {
  func isPalindrome(_ s: String) -> Bool {
    if let regex = try? NSRegularExpression(pattern: "[a-zA-Z0-9]+") {
      let string = regex
        .matches(in: s, range: .init(location: 0, length: s.count))
        .map { s[Range($0.range, in: s)!].lowercased() }
        .joined()

      return string == String(string.reversed())
    }

    return false
  }

  func isPalindromeUsingRegexString(_ s: String) -> Bool {
    var alphabets = ""
    for match in s.matches(of: /(?<alphabet>[a-zA-Z0-9]+)/) {
      alphabets += match.alphabet.lowercased()
    }
    return String(alphabets.reversed()) == alphabets
  }
}
