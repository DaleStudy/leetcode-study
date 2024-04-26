//
//  121. Best Time to Buy and Sell Stock.swift
//  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/04/26.
//

import Foundation

final class LeetCode121 {
  func maxProfit(_ prices: [Int]) -> Int {
    if prices.count == 1 { return 0 }
    var diff = 0
    var left = 0
    var right = 0

    while right < prices.endIndex {
      if prices[left] > prices[right] {
        left = right
      } else {
        diff = max(diff, prices[right] - prices[left])
      }
      right += 1
    }
    return diff
  }
}
