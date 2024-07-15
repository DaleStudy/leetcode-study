//  
//  647. Palindromic Substrings
//  https://leetcode.com/problems/palindromic-substrings/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/14.
//  

class Solution {

  // dp way
  func countSubstringsUsingDP(_ s: String) -> Int {
    let array = Array(s)
    let n = array.count
    var count = 0

    var dp: [[Bool]] = .init(
      repeating: .init(repeating: false, count: n),
      count: n
    )

    for i in dp.indices {
      dp[i][i] = true
      count += 1
    }

    for i in dp.indices.dropLast() where array[i] == array[i + 1] {
      dp[i][i + 1] = true
      count += 1
    }

    for length in stride(from: 3, through: n, by: 1) {
      for i in 0 ... n - length where array[i] == array[i + length - 1] && dp[i + 1][i + length - 2] {
        dp[i][i + length - 1] = true
        count += 1
      }
    }

    return count
  }

  // center and expand way
  func countSubstrings(_ s: String) -> Int {
    let array = Array(s)
    var count = 0

    for startIndex in array.indices {
      let evenCount = expandAroundCenter(array, startIndex, startIndex + 1)
      let oddCount = expandAroundCenter(array, startIndex, startIndex)
      count += evenCount + oddCount
    }

    return count
  }

  private func expandAroundCenter(_ array: [Character], _ left: Int, _ right: Int) -> Int {
    var count = 0
    var l = left
    var r = right
    while l >= 0 && r < array.count && array[l] == array[r] {
      l -= 1
      r += 1
      count += 1
    }

    return count
  }

  
  // Brute Force
  func countSubstringsUsingBruteForce(_ s: String) -> Int {
    let array = Array(s)
    var count = 0

    for startIndex in array.indices {
      for targetIndex in startIndex ..< array.count where array[startIndex] == array[targetIndex] {
        if isPalindrome(
          array,
          startIndex,
          targetIndex
        ) {
          count += 1
        }
      }
    }

    return count
  }

  private func isPalindrome(_ array: [Character], _ start: Int, _ end: Int) -> Bool {
    var startIndex = start
    var endIndex = end
    while startIndex < endIndex {
      if array[startIndex] == array[endIndex] {
        startIndex += 1
        endIndex -= 1
        continue
      }

      return false
    }

    return true
  }
}
