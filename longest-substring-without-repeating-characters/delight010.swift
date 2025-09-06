class Solution {
    // Time complexity O(N)
    // Space complexity O(min(m,n))
    func lengthOfLongestSubstring(_ s: String) -> Int {
        if s.isEmpty {
            return 0
        }
        var maxLength = 0
        var startIndex = 0
        var charSet: Set<Character> = []
        let charArray = Array(s)
        
        for right in 0..<charArray.count {
            while charSet.contains(charArray[right]) {
                charSet.remove(charArray[startIndex])
                startIndex += 1
            }
            
            charSet.insert(charArray[right])
            maxLength = max(maxLength, right - startIndex + 1)
        }
        
        return maxLength
    }
}
 
