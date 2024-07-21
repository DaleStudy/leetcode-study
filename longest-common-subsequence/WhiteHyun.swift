//  
//  1143. Longest Common Subsequence
//  https://leetcode.com/problems/longest-common-subsequence/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/20.
//  

class Solution {
  func longestCommonSubsequence(_ text1: String, _ text2: String) -> Int {
    let m = text1.count
    let n = text2.count

    var dp: [[Int]] = .init(repeating: .init(repeating: 0, count: n + 1), count: m + 1)

    let text1Array = Array(text1)
    let text2Array = Array(text2)

    for i in 1 ... m {
      for j in 1 ... n {
        if text1Array[i - 1] == text2Array[j - 1] {
          dp[i][j] = dp[i - 1][j - 1] + 1
        } else {
          dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        }
      }
    }

    return dp[m][n]
  }
}
