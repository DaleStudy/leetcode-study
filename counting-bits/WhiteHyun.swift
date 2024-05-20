//  
//  338. Counting Bits
//  https://leetcode.com/problems/counting-bits/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/19.
//  

final class Solution {

  // MARK: - Time Complexity: O(n), Space Complexity: O(n)

  func countBits(_ n: Int) -> [Int] {
    var array: [Int] = .init(repeating: 0, count: n + 1)
    for i in stride(from: 1, through: n, by: 1) {
      array[i] = array[i >> 1] + (i & 1)
    }
    return array
  }

  // MARK: - nonzeroBitCount

  func countBits2(_ n: Int) -> [Int] {
    return (0...n).map(\.nonzeroBitCount)
  }

}
