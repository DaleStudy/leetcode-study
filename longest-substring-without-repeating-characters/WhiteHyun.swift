//  
//  3. Longest Substring Without Repeating Characters
//  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/08.
//  

class Solution {
  func lengthOfLongestSubstring(_ s: String) -> Int {
    var longest: Int = .min
    let array = Array(s)

    var set: Set<Character> = []
    var startIndex = 0
    for index in array.indices {
      if set.contains(array[index]) == false {
        set.insert(array[index])
        continue
      }

      if longest < index - startIndex {
        longest = index - startIndex
      }

      while array[startIndex] != array[index] {
        set.remove(array[startIndex])
        startIndex += 1
      }
      startIndex += 1
    }

    if longest < array.endIndex - startIndex {
      longest = array.endIndex - startIndex
    }


    return longest
  }
}
