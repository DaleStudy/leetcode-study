//  
//  191. Number of 1 Bits
//  https://leetcode.com/problems/number-of-1-bits/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/19.
//  

final class Solution {
  func hammingWeight(_ n: Int) -> Int {
    n.nonzeroBitCount
  }
  
  func hammingWeight2(_ n: Int) -> Int {
    var number = n
    var answer = 0
    while number != 0 {
      answer += number & 1
      number >>= 1
    }

    return answer
  }
}
