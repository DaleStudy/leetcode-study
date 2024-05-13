//  
//  70. Climbing Stairs
//  https://leetcode.com/problems/climbing-stairs/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/12.
//  

final class Solution {
  func climbStairs(_ n: Int) -> Int {
    var prevWays = 1
    var prevPrevWays = 1
    for _ in stride(from: 2, through: n, by: 1) {
      (prevWays, prevPrevWays) = (prevPrevWays, prevWays + prevPrevWays)
    }
    return prevPrevWays
  }
}
