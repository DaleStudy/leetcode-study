//  
//  91. Decode Ways
//  https://leetcode.com/problems/decode-ways/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/07/14.
//  

class Solution {

  // dp
  func numDecodings(_ s: String) -> Int {
    var (current, previous) = (1, 0)
    let array = s.compactMap { Int(String($0)) }
    for index in array.indices.reversed() {
      if array[index] == 0 {
        (current, previous) = (0, current)
      } else if index + 1 < array.count, array[index] * 10 + array[index + 1] <= 26 {
        (current, previous) = (current + previous, current)
      } else {
        previous = current
      }
    }

    return current
  }

  // Memoization
  func numDecodingsUsingMemoization(_ s: String) -> Int {
    let messages = s.compactMap { Int(String($0)) }
    var cache: [Int: Int] = [s.count: 1]

    func dfs(_ index: Int) -> Int {
      if let cached = cache[index] {
        return cached
      }

      if messages[index] == 0 {
        cache[index] = 0
      } else if index + 1 < s.count && messages[index] * 10 + messages[index + 1] < 27 {
        cache[index] = dfs(index + 1) + dfs(index + 2)
      } else {
        cache[index] = dfs(index + 1)
      }
      return cache[index]!
    }

    return dfs(0)
  }
}
