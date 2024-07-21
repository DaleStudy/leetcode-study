//  
//  53. Maximum Subarray
//  https://leetcode.com/problems/maximum-subarray/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/20.
//  

class Solution {
  func maxSubArray(_ numbers: [Int]) -> Int {
    var tracking = numbers[0]
    var answer = numbers[0]
    for value in numbers.dropFirst() {
      tracking = max(tracking + value, value)
      if tracking > answer {
        answer = tracking
      }
    }

    return answer
  }
}
