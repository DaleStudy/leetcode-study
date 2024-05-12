//  
//  70. Climbing Stairs
//  https://leetcode.com/problems/climbing-stairs/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/12.
//  

final class Solution {
  func climbStairs(_ n: Int) -> Int {
    var dp: [Int] = .init(repeating: 0, count: 45)
    dp[0] = 1
    dp[1] = 2
    for i in 2 ..< 45 {
      dp[i] = dp[i - 1] + dp[i - 2]
    }
    return dp[n - 1]
  }
}
