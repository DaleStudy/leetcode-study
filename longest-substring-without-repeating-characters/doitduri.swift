class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var charIndexMap = [Character: Int]()
        var maxLength = 0
        var startIndex = 0
        
        for (i, char) in Array(s).enumerated() {
            if let lastIndex = charIndexMap[char], lastIndex >= startIndex {
                startIndex = lastIndex + 1
            }
            
            let currentLength = i - startIndex + 1
            maxLength = max(maxLength, currentLength)
            
            charIndexMap[char] = i
        }
        
        return maxLength
    }
}
