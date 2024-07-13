//  
//  322. Coin Change
//  https://leetcode.com/problems/coin-change/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/14.
//  

class Solution {
  func coinChange(_ coins: [Int], _ amount: Int) -> Int {
    var dp: [Int] = .init(repeating: .max, count: amount + 1)

    dp[0] = 0

    for coin in coins {
      for index in stride(from: coin, to: dp.count, by: 1) where dp[index - coin] != .max && dp[index - coin] + 1 < dp[index] {
        dp[index] = dp[index - coin] + 1
      }
    }

    return dp.last == .max ? -1 : dp.last!
  }
}
