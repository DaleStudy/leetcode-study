//  
//  49. Group Anagrams
//  https://leetcode.com/problems/group-anagrams/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/19.
//  

final class Solution {
  func groupAnagrams(_ strs: [String]) -> [[String]] {
    var dictionary: [String: [String]] = [:]
    for str in strs {
      dictionary[String(str.sorted()), default: []].append(str)
    }

    return Array(dictionary.values)
  }
}
