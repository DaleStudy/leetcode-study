//  
//  5. Longest Palindromic Substring
//  https://leetcode.com/problems/longest-palindromic-substring/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/06.
//  

class Solution {
  func longestPalindrome(_ s: String) -> String {
    let array = Array(s)
    if array.count == 1 { return s }

    var start = 0
    var maxLength = 1

    func expandAroundCenter(_ left: Int, _ right: Int) -> Int {
      var l = left
      var r = right
      while l >= 0, r < array.count, array[l] == array[r] {
        l -= 1
        r += 1
      }
      return r - l - 1
    }

    for index in array.indices {
      let length1 = expandAroundCenter(index, index) // 홀수 길이
      let length2 = expandAroundCenter(index, index + 1) // 짝수 길이
      let length = max(length1, length2)

      if length > maxLength {
        start = index - (length - 1) / 2
        maxLength = length
      }
    }
    return String(array[start ..< start + maxLength])
  }
}
