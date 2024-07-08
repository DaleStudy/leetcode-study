//  
//  198. House Robber
//  https://leetcode.com/problems/house-robber/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/06.
//  

class Solution {
  func rob(_ nums: [Int]) -> Int {
    var previous = 0
    var current = 0

    for element in nums {
      (previous, current) = (current, max(element + previous, current))
    }
    return max(previous, current)
  }
}
