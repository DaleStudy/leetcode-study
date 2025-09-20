class Solution {
    // O(n) time / O(n) space
    func characterReplacement(_ s: String, _ k: Int) -> Int {
        var windowStart = 0
        var maxLength = 0
        var maxCharacterRepeat = 0
        var countByCharacter = [Character: Int]()
        var characters = Array(s)
        
        for windowEnd in 0..<characters.count {
            countByCharacter[characters[windowEnd], default: 0] += 1
            maxCharacterRepeat = max(maxCharacterRepeat, countByCharacter[characters[windowEnd]]!)
            
            var length = windowEnd - windowStart + 1
            if length - maxCharacterRepeat <= k {
                maxLength = max(maxLength, length)
            } else {
                while (windowEnd - windowStart + 1) - maxCharacterRepeat > k {
                    countByCharacter[characters[windowStart]]! -= 1
                    windowStart += 1
                }
            }
        }
        return maxLength
    }
}
