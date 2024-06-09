//  
//  424. Longest Repeating Character Replacement
//  https://leetcode.com/problems/longest-repeating-character-replacement/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/08.
//  

final class Solution {
  func characterReplacement(_ s: String, _ k: Int) -> Int {
    var maxFrequency = 0
    var i = 0
    var counter: [Character: Int] = [:]
    let array = Array(s)

    for index in array.indices {
      counter[array[index], default: 0] += 1
      if maxFrequency < counter[array[index]]! {
        maxFrequency = counter[array[index]]!
      }

      if index - i + 1 > maxFrequency + k {
        counter[array[i]]! -= 1
        i += 1
      }
    }

    return array.count - i
  }
}
