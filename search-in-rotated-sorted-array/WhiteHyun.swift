//  
//  33. Search in Rotated Sorted Array
//  https://leetcode.com/problems/search-in-rotated-sorted-array/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/10.
//  

final class Solution {
  func search(_ nums: [Int], _ target: Int) -> Int {
    guard nums.count != 1
    else {
      return nums[0] == target ? 0 : -1
    }

    var left = 0
    var right = nums.count - 1

    while left <= right {
      let mid = (left + right) >> 1

      if nums[mid] == target { return mid }

      if nums[left] <= nums[mid] {
        if target > nums[mid] || target < nums[left] {
          left = mid + 1
        } else {
          right = mid - 1
        }
      } else {
        if target < nums[mid] || target > nums[right] {
          right = mid - 1
        } else {
          left = mid + 1
        }
      }
    }

    return -1
  }
}
