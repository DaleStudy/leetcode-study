//  
//  11. Container With Most Water
//  https://leetcode.com/problems/container-with-most-water/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/08.
//  

class Solution {
  func maxArea(_ height: [Int]) -> Int {
    var totalArea = 0
    var left = 0
    var right = height.endIndex - 1

    while left < right {
      let area = (right - left) * min(height[left], height[right])
      if area > totalArea {
        totalArea = area
      }

      if height[left] < height[right] {
        left += 1
      } else {
        right -= 1
      }
    }

    return totalArea
  }
}
