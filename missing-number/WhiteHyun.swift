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

  func missingNumber2(_ nums: [Int]) -> Int {
    nums.count * (nums.count + 1) / 2 - nums.reduce(0, +)
  }

  func missingNumber3(_ nums: [Int]) -> Int {
    Set(0...nums.count).subtracting(Set(nums)).first!
  }

  func missingNumber4(_ nums: [Int]) -> Int {
    var answer = 0
    for i in 0 ..< nums.count {
      answer = answer ^ i ^ nums[i]
    }

    return answer ^ nums.count
  }
}
