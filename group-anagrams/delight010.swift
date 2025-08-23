class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var dict: [[Character: Int]: [String]] = [:]
        for str in strs {
            var strDict: [Character: Int] = [:]
            for char in str {
                if let charCount = strDict[char] {
                    strDict[char] = charCount + 1
                } else {
                    strDict[char] = 1
                }
            }
            if dict[strDict] != nil {
                dict[strDict]?.append(str)
            } else {
                dict[strDict] = [str]
            }
        }
        
        return dict.values.map { $0 }
    }
}
 
