//  
//  213. House Robber II
//  https://leetcode.com/problems/house-robber-ii/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/06.
//  

class Solution {
  func rob(_ nums: [Int]) -> Int {
    if nums.count < 3 { return nums.max()! }
    var current = 0
    var previous = 0
    
    // 첫 번째 집을 턴 경우
    for element in nums.dropLast() {
      (previous, current) = (current, max(element + previous, current))
    }

    var current2 = 0
    var previous2 = 0

    // 첫 번째 집을 털지 않은 경우
    for element in nums.dropFirst() {
      (previous2, current2) = (current2, max(element + previous2, current2))
    }

    return max(current, previous, current2, previous2)
  }
}
