//  
//  152. Maximum Product Subarray
//  https://leetcode.com/problems/maximum-product-subarray/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/14.
//  

class Solution {
  func maxProduct(_ nums: [Int]) -> Int {
    var maxNumber = nums[0]
    var minNumber = nums[0]
    var answer = nums[0]
    // Problem 190 / 191 방어 코드
    let negativeCount = nums.filter { $0 < 0 }.count


    for index in 1 ..< nums.count {
      let current = nums[index]

      let tempMin = minNumber
      let tempMax = maxNumber

      maxNumber = max(current, tempMin * current, tempMax * current)
      if negativeCount > 1 {
        minNumber = min(current, tempMin * current, tempMax * current)
      } else {
        minNumber = 0
      }
      if answer < maxNumber {
        answer = maxNumber
      }
    }

    return answer
  }

}
