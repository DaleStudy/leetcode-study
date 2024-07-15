//  
//  139. Word Break
//  https://leetcode.com/problems/word-break/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/14.
//  

class Solution {
  func wordBreak(_ s: String, _ wordDict: [String]) -> Bool {
    var cache: [String: Bool] = [:]

    func helper(_ string: String) -> Bool {
      if let result = cache[string] {
        return result
      }

      if string.isEmpty {
        cache[string] = true
        return true
      }

      for word in wordDict where string.hasPrefix(word) {
        if helper(String(string.dropFirst(word.count))) {
          cache[string] = true
          return true
        }
      }

      cache[string] = false
      return false
    }

    return helper(s)
  }
}
