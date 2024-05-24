//  
//  268. Missing Number
//  https://leetcode.com/problems/missing-number/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/19.
//  

final class Solution {
  func missingNumber(_ nums: [Int]) -> Int {
    (0 ... nums.count).reduce(0, +) - nums.reduce(0, +)
  }
}
