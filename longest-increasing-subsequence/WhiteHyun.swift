//  
//  300. Longest Increasing Subsequence
//  https://leetcode.com/problems/longest-increasing-subsequence/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/20.
//  

class Solution {
  func lengthOfLIS(_ nums: [Int]) -> Int {
    var tails: [Int] = [nums[0]]

    for index in 1 ..< nums.count {
      if nums[index] > tails.last! {
        tails.append(nums[index])
      } else {
        tails[binarySearch(tails, target: nums[index])] = nums[index]
      }
    }

    return tails.count
  }

  private func binarySearch(_ arr: [Int], target: Int) -> Int {
    var left = 0
    var right = arr.count - 1

    while left <= right {
      let mid = (left + right) >> 1
      if arr[mid] < target {
        left = mid + 1
      } else {
        right = mid - 1
      }
    }
    return left
  }
}
