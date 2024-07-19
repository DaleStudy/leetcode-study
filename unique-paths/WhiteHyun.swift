//  
//  62. Unique Paths
//  https://leetcode.com/problems/unique-paths/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/20.
//  

class Solution {
  func uniquePaths(_ m: Int, _ n: Int) -> Int {
    if m == 1 || n == 1 { return 1 }
    var dp: [[Int]] = .init(repeating: .init(repeating: 1, count: n), count: m)

    for i in 1 ..< m {
      for j in 1 ..< n {
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
      }
    }

    return dp[m - 1][n - 1]
  }
}
