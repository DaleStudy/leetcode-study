//  
//  190. Reverse Bits
//  https://leetcode.com/problems/reverse-bits/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/19.
//  

final class Solution {

  // MARK: - Runtime: 5ms / Memory 16.12 MB

  func reverseBits(_ n: Int) -> Int {
    let reversedStringBits = String(String(n, radix: 2).reversed())
    return Int(reversedStringBits + String(repeating: "0", count: 32 - reversedStringBits.count), radix: 2)!
  }

  // MARK: - Runtime: 5ms / Memory 15.72 MB

  func reverseBits2(_ n: Int) -> Int {
    var answer = 0

    for index in 0 ..< 32 {
      answer += ((n >> (32 - index - 1)) & 1) << index
    }
    return answer
  }
}
