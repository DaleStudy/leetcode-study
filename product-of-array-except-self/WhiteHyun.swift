//  
//  238. Product of Array Except Self
//  https://leetcode.com/problems/product-of-array-except-self/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/01.
//  

final class Solution {
  func productExceptSelf(_ nums: [Int]) -> [Int] {
    var answer: [Int] = .init(repeating: 1, count: nums.count)

    var left_product = 1
    for i in nums.indices {
      answer[i] = left_product
      left_product *= nums[i]
    }

    var right_product = 1
    for i in nums.indices.reversed() {
      answer[i] *= right_product
      right_product *= nums[i]
    }

    return answer
  }
}
